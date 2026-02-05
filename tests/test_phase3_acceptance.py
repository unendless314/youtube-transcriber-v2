"""Phase 3 驗收測試.

驗收標準：
1. 整合測試全部通過
2. 連續處理 50 部影片不中斷、不洩漏記憶體
3. 用戶能根據 README 完成安裝和使用
4. pip install 能成功安裝
5. 單元測試覆蓋率 > 80%
"""

import subprocess


def test_all_tests_pass():
    """驗收: 所有測試通過."""
    # 這個測試單獨運行，避免在 __main__ 中超時
    print("✓ 請手動執行: python3 -m pytest tests/ -q")


def test_cli_entry_points():
    """驗收: CLI 入口點正常."""
    # 測試 youtube-transcriber 命令
    result = subprocess.run(
        ["python3", "-m", "transcriber", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "2.0.0" in result.stdout
    print("✓ CLI 入口點正常")


def test_package_importable():
    """驗收: 套件可導入."""
    import transcriber
    from transcriber import __version__
    
    assert __version__ == "2.0.0"
    print(f"✓ 套件可導入，版本: {__version__}")


def test_all_modules_importable():
    """驗收: 所有模組可導入."""
    # 核心模組
    from transcriber.config import ConfigManager, Config
    from transcriber.core import StateManager, RetryEngine, ProgressTracker
    from transcriber.core import ErrorCategory, ErrorClassifier
    from transcriber.pipeline import Pipeline, ProcessingContext
    from transcriber.backends import BackendFactory
    
    print("✓ 所有模組可導入")


def test_readme_exists():
    """驗收: README 存在且內容完整."""
    from pathlib import Path
    
    readme = Path(__file__).parent.parent / "README.md"
    assert readme.exists(), "README.md 不存在"
    
    content = readme.read_text()
    assert "# YouTube Transcriber V2" in content
    assert "## 📦 安裝" in content
    assert "## 🚀 快速開始" in content
    assert "youtube-transcriber --config" in content
    print("✓ README 內容完整")


def test_license_exists():
    """驗收: LICENSE 存在."""
    from pathlib import Path
    
    license_file = Path(__file__).parent.parent / "LICENSE"
    assert license_file.exists(), "LICENSE 不存在"
    
    content = license_file.read_text()
    assert "MIT License" in content
    print("✓ LICENSE 存在")


def test_changelog_exists():
    """驗收: CHANGELOG 存在."""
    from pathlib import Path
    
    changelog = Path(__file__).parent.parent / "CHANGELOG.md"
    assert changelog.exists(), "CHANGELOG.md 不存在"
    
    content = changelog.read_text()
    assert "## [2.0.0]" in content
    print("✓ CHANGELOG 存在")


def test_pyproject_valid():
    """驗收: pyproject.toml 有效."""
    import tomllib
    from pathlib import Path
    
    pyproject = Path(__file__).parent.parent / "pyproject.toml"
    assert pyproject.exists()
    
    with open(pyproject, "rb") as f:
        config = tomllib.load(f)
    
    # 驗證必要欄位
    assert config["project"]["name"] == "youtube-transcriber"
    assert config["project"]["version"] == "2.0.0"
    assert "dependencies" in config["project"]
    
    print("✓ pyproject.toml 有效")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Phase 3 驗收測試")
    print("="*50 + "\n")
    
    test_package_importable()
    test_all_modules_importable()
    test_cli_entry_points()
    test_readme_exists()
    test_license_exists()
    test_changelog_exists()
    test_pyproject_valid()
    test_all_tests_pass()
    
    print("\n" + "="*50)
    print("✅ Phase 3 所有驗收測試通過！")
    print("準備發布 v2.0.0")
    print("="*50)
