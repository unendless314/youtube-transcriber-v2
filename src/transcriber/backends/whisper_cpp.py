"""whisper.cpp 後端實作 - 透過 CLI 執行檔串接."""

import re
import subprocess
import tempfile
from pathlib import Path

import structlog

from transcriber.backends.base import (
    TranscriptionResult,
    TranscriptionSegment,
    WhisperBackend,
)
from transcriber.core.errors import ErrorCategory, TranscribeError

logger = structlog.get_logger(__name__)


class WhisperCppBackend(WhisperBackend):
    """whisper.cpp 後端 - 直接呼叫編譯好的 CLI 執行檔."""
    
    def __init__(
        self, 
        model: str, 
        language: str | None = None,
        cpp_bin: Path | None = None,
        model_path: Path | None = None
    ) -> None:
        super().__init__(model, language)
        self.cpp_bin = cpp_bin
        self.model_path = model_path
        self.logger = structlog.get_logger(__name__, backend="whisper.cpp")
    
    @property
    def name(self) -> str:
        return "whisper.cpp"
    
    def load(self) -> None:
        """檢查執行檔與模型是否存在."""
        if not self.cpp_bin or not self.cpp_bin.exists():
            raise TranscribeError(
                f"找不到 whisper.cpp 執行檔: {self.cpp_bin}",
                category=ErrorCategory.SYSTEM,
            )
        
        if not self.model_path or not self.model_path.exists():
            raise TranscribeError(
                f"找不到模型檔案: {self.model_path}",
                category=ErrorCategory.SYSTEM,
            )
        
        self._is_loaded = True
        self.logger.info("backend_ready", bin=str(self.cpp_bin), model=str(self.model_path))
    
    def transcribe(self, audio_path: Path) -> TranscriptionResult:
        """轉錄音訊.
        
        流程:
        1. 使用 ffmpeg 轉換為 16kHz WAV (whisper.cpp 要求)
        2. 執行 whisper-cli (使用 -osrt 以獲得時間戳)
        3. 解析 SRT 輸出為 segments
        """
        if not self.is_loaded:
            self.load()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            wav_path = tmp_path / "input.wav"
            output_base = tmp_path / "output"
            
            # 1. 轉換音訊格式
            self._convert_to_wav(audio_path, wav_path)
            
            # 2. 準備指令 — 使用 -osrt 以獲得每個 segment 的時間戳
            cmd = [
                str(self.cpp_bin),
                "-m", str(self.model_path),
                "-f", str(wav_path),
                "-l", self.language if self.language and self.language != "auto" else "auto",
                "-osrt",
                "-of", str(output_base)
            ]
            
            self.logger.info("executing_whisper_cpp", command=" ".join(cmd))
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                # 3. 讀取並解析 SRT 結果
                srt_file = tmp_path / "output.srt"
                if not srt_file.exists():
                    raise TranscribeError(
                        f"whisper.cpp 執行成功但未產生輸出檔案: {result.stderr}",
                        category=ErrorCategory.SYSTEM,
                    )
                
                srt_content = srt_file.read_text(encoding="utf-8").strip()
                segments = self._parse_srt(srt_content)
                
                if not segments:
                    raise TranscribeError(
                        "SRT 解析結果為空",
                        category=ErrorCategory.SYSTEM,
                    )
                
                # 合併所有 segment 文字作為完整文本
                full_text = " ".join(seg.text for seg in segments)
                
                return TranscriptionResult(
                    text=full_text,
                    language=self.language or "auto",
                    segments=segments,
                )
                
            except subprocess.CalledProcessError as e:
                self.logger.error("whisper_cpp_failed", stdout=e.stdout, stderr=e.stderr)
                category = self._classify_error(e.stderr or "")
                raise TranscribeError(
                    f"whisper.cpp 執行失敗: {e.stderr}",
                    category=category,
                )
    
    def _parse_srt(self, srt_text: str) -> list[TranscriptionSegment]:
        """解析 SRT 格式為 TranscriptionSegment 列表.
        
        SRT 格式範例:
            1
            00:00:00,000 --> 00:00:08,960
             It's my distinct honor to once again administer the oath
        """
        timecode_pattern = re.compile(
            r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})'
        )
        
        segments: list[TranscriptionSegment] = []
        blocks = re.split(r'\n\s*\n', srt_text.strip())
        
        for block in blocks:
            if not block.strip():
                continue
            
            lines = block.strip().split('\n')
            if len(lines) < 3:
                continue
            
            try:
                timecode_match = timecode_pattern.search(lines[1])
                if not timecode_match:
                    continue
                
                start_tc, end_tc = timecode_match.groups()
                start_sec = self._srt_timecode_to_seconds(start_tc)
                end_sec = self._srt_timecode_to_seconds(end_tc)
                
                # 合併多行文字為單行
                text = ' '.join(line.strip() for line in lines[2:]).strip()
                
                if text:
                    segments.append(TranscriptionSegment(
                        start=start_sec,
                        end=end_sec,
                        text=text,
                    ))
            except (ValueError, IndexError) as e:
                self.logger.warning("srt_parse_warning", error=str(e), block=block[:80])
                continue
        
        self.logger.info("srt_parsed", segment_count=len(segments))
        return segments
    
    @staticmethod
    def _srt_timecode_to_seconds(timecode: str) -> float:
        """將 SRT 時間碼 (HH:MM:SS,mmm) 轉換為秒數."""
        time_part, ms_part = timecode.split(',')
        h, m, s = map(int, time_part.split(':'))
        ms = int(ms_part)
        return h * 3600 + m * 60 + s + ms / 1000.0

    def _classify_error(self, error_msg: str) -> ErrorCategory:
        """根據錯誤訊息分類錯誤類型."""
        error_lower = error_msg.lower()
        
        # 記憶體不足
        if any(kw in error_lower for kw in ["out of memory", "oom", "cannot allocate", "bad alloc"]):
            return ErrorCategory.SYSTEM  # 視為系統資源問題
        
        # 模型相關錯誤
        if any(kw in error_lower for kw in ["model", "ggml", "tensor", "checkpoint"]):
            return ErrorCategory.SYSTEM
        
        # 輸入音訊問題
        if any(kw in error_lower for kw in ["audio", "wav", "ffmpeg", "format", "codec"]):
            return ErrorCategory.VIDEO  # 音訊處理問題視為影片問題
        
        return ErrorCategory.SYSTEM
    
    def _convert_to_wav(self, input_path: Path, output_path: Path) -> None:
        """使用 ffmpeg 將音訊轉換為 16kHz mono WAV."""
        cmd = [
            "ffmpeg", "-y",
            "-i", str(input_path),
            "-ar", "16000",
            "-ac", "1",
            "-c:a", "pcm_s16le",
            str(output_path)
        ]
        try:
            subprocess.run(cmd, capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            raise TranscribeError(
                f"音訊轉換失敗 (ffmpeg): {e.stderr.decode()}",
                category=ErrorCategory.SYSTEM,
            )
        except FileNotFoundError:
            raise TranscribeError(
                "找不到 ffmpeg 執行檔，請先安裝 ffmpeg",
                category=ErrorCategory.SYSTEM,
            )