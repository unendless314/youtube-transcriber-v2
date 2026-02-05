"""Pipeline Orchestrator - 協調各 Stage 的執行."""

from pathlib import Path
from typing import Any

import structlog

from transcriber.config.models import Config
from transcriber.core.errors import (
    ErrorCategory,
    ErrorClassifier,
    TranscriberError,
)
from transcriber.core.state import StateManager, VideoStatus
from transcriber.pipeline.context import ProcessingContext
from transcriber.pipeline.stages import (
    CleanupStage,
    DownloadStage,
    SaveStage,
    Stage,
    TranscribeStage,
)

logger = structlog.get_logger(__name__)


class Pipeline:
    """處理 Pipeline - 協調多個 Stage 的執行."""
    
    def __init__(self, config: Config, state_manager: StateManager) -> None:
        self.config = config
        self.state = state_manager
        self.stages: list[Stage] = []
        self.logger = structlog.get_logger(__name__)
    
    def add_stage(self, stage: Stage) -> "Pipeline":
        """加入 Stage.
        
        Args:
            stage: Stage 實例
            
        Returns:
            self，支援鏈式呼叫
        """
        self.stages.append(stage)
        return self
    
    def process(self, context: ProcessingContext) -> ProcessingContext:
        """處理單一影片.
        
        執行流程：
        1. 檢查是否已處理（is_processed）
        2. 依序執行各 Stage
        3. 標記完成或失敗
        4. 錯誤處理與分類
        
        Args:
            context: 處理上下文
            
        Returns:
            更新後的上下文
            
        Raises:
            TranscriberError: 若錯誤分類為 SYSTEM 或達到最大重試次數
        """
        # 檢查是否已處理
        if self.state.is_processed(context.video_id):
            self.logger.info("video_already_processed", video_id=context.video_id)
            return context
        
        # 註冊影片到狀態管理
        self.state.mark_pending(
            context.video_id,
            context.channel_name,
            context.title,
            metadata=context.to_metadata(),
        )
        
        self.logger.info(
            "pipeline_started",
            video_id=context.video_id,
            title=context.title,
            channel=context.channel_name,
        )
        
        try:
            # 依序執行各 Stage
            for stage in self.stages:
                self.logger.debug("stage_start", stage=stage.name, video_id=context.video_id)
                
                # 檢查是否需要跳過
                if stage.should_skip(context):
                    self.logger.debug("stage_skipped", stage=stage.name, video_id=context.video_id)
                    continue
                
                # 執行 Stage
                context = stage.execute(context)
                context.stage_results[stage.name] = "success"
                
                self.logger.debug("stage_complete", stage=stage.name, video_id=context.video_id)
            
            # 全部完成
            self.state.mark_completed(context.video_id, str(context.output_path) if context.output_path else None)
            self.logger.info(
                "pipeline_completed",
                video_id=context.video_id,
                output_path=str(context.output_path) if context.output_path else None,
            )
            
        except TranscriberError as e:
            # 已知錯誤，記錄並重新拋出
            self._handle_error(context, e)
            raise
            
        except Exception as e:
            # 未知錯誤，分類後處理
            category = ErrorClassifier.classify(e)
            error = TranscriberError(str(e), category)
            self._handle_error(context, error)
            raise error from e
        
        return context
    
    def _handle_error(self, context: ProcessingContext, error: TranscriberError) -> None:
        """處理錯誤.
        
        Args:
            context: 處理上下文
            error: 錯誤物件
        """
        self.logger.error(
            "pipeline_error",
            video_id=context.video_id,
            error=error.message,
            category=error.category.name,
        )
        
        # 更新狀態為失敗
        self.state.mark_status(
            context.video_id,
            VideoStatus.FAILED,
            error_message=error.message,
            error_category=error.category.name,
        )


def create_default_pipeline(config: Config, state_manager: StateManager) -> Pipeline:
    """建立預設的處理 Pipeline.
    
    Args:
        config: 配置物件
        state_manager: 狀態管理器
        
    Returns:
        配置好的 Pipeline
    """
    pipeline = Pipeline(config, state_manager)
    pipeline.add_stage(DownloadStage(config, state_manager))
    pipeline.add_stage(TranscribeStage(config, state_manager))
    pipeline.add_stage(SaveStage(config, state_manager))
    pipeline.add_stage(CleanupStage(config, state_manager))
    return pipeline
