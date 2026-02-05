# GEMINI.md - YouTube Transcriber V2

## Project Overview
YouTube Transcriber V2 is a production-grade tool designed to automatically track YouTube channels and transcribe their videos using Whisper AI. It prioritizes reliability and persistence, featuring a robust breakpoint resume system powered by SQLite and a modular pipeline architecture.

### Main Technologies
- **Language:** Python 3.9+
- **CLI Framework:** [Click](https://click.palletsprojects.com/)
- **UI/Progress:** [Rich](https://rich.readthedocs.io/)
- **Configuration:** [Pydantic](https://docs.pydantic.dev/) & YAML
- **Downloading:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **AI Transcription:** [OpenAI Whisper](https://github.com/openai/whisper) (with support for `whisper.cpp` and `faster-whisper`)
- **Persistence:** SQLite (for state management and resuming)
- **Logging:** [structlog](https://www.structlog.org/) (structured logging)

### Architecture
The project follows a stage-based pipeline architecture:
1.  **Orchestrator:** Coordinates the execution of stages for each video.
2.  **Stages (`src/transcriber/pipeline/stages.py`):**
    - `DownloadStage`: Fetches audio using `yt-dlp`.
    - `TranscribeStage`: Converts audio to text via a Whisper backend.
    - `SaveStage`: Formats and saves the transcript as Markdown.
    - `CleanupStage`: Removes temporary audio files.
3.  **Backends:** Pluggable transcription engines (OpenAI, C++, Faster).
4.  **Core Services:**
    - `StateManager`: SQLite-based status tracking (`pending`, `downloading`, `completed`, etc.).
    - `ErrorClassifier`: Categorizes exceptions (Network, Rate Limit, System, etc.) for intelligent retries.
    - `RetryHandler`: Implements exponential backoff with jitter.

## Building and Running

### Setup
```bash
# Install dependencies with OpenAI Whisper support and dev tools
pip install -e ".[openai-whisper,dev]"
```

### Key Commands
- **Initialize Config:** `youtube-transcriber --init-config channels.yaml`
- **Run Transcriber:** `youtube-transcriber --config channels.yaml`
- **Dry Run:** `youtube-transcriber --config channels.yaml --dry-run`
- **Run Tests:** `pytest`
- **Linting:** `ruff check .`
- **Type Checking:** `mypy src/`

## Development Conventions

### Coding Style
- **Formatting:** Managed by `ruff` (line length 100).
- **Docstrings:** Follows the **Google Style** convention.
- **Type Hints:** Required for all function definitions (`disallow_untyped_defs = true` in `mypy`).
- **Logging:** Use `structlog` for all logs to ensure they are structured and searchable.

### Testing Practices
- **Framework:** `pytest`
- **Structure:** 
    - `tests/unit/`: Logic-specific tests (config, state, retry).
    - `tests/integration/`: End-to-end pipeline and error handling tests.
    - `tests/test_phase*.py`: Acceptance tests for specific development milestones.
- **Coverage:** Aim for >80% coverage on core modules (`src/transcriber/core`, `src/transcriber/pipeline`).

### State Management
- All video processing states must be recorded in the SQLite database to ensure "resume-from-failure" capability (breakpoint resume).
- Use `StateManager` to query or update status rather than direct SQL if possible.

### Error Handling
- Never catch-all `Exception` without re-raising or classifying it via `ErrorClassifier`.
- Errors should be categorized into `NETWORK`, `RATE_LIMIT`, `RESOURCE`, `VIDEO`, or `SYSTEM` to trigger the appropriate retry strategy.
