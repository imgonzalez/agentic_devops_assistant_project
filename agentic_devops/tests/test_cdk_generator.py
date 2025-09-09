import shutil
import tempfile
from pathlib import Path
import pytest
from agentic_devops.generator.cdk_generator import CDKGenerator

class DummyLogger:
    def info(self, msg): pass
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass
    def exception(self, msg): pass
    def success(self, msg): pass

def test_generate_project_creates_files(monkeypatch):
    # Setup temp dir
    temp_dir = tempfile.mkdtemp()
    project_path = Path(temp_dir) / "test_project"
    stack_template_name = "api_rest_python"

    # Patch logger
    monkeypatch.setattr("agentic_devops.generator.cdk_generator.logger", DummyLogger())

    # Run generator
    generator = CDKGenerator(project_path, stack_template_name)
    generator.generate_project()

    # Check expected files
    assert (project_path / "bin/app.py").exists()
    assert (project_path / "lib/api_rest_stack.py").exists()
    assert (project_path / "requirements.txt").exists()
    shutil.rmtree(temp_dir)
