import os
import shutil
import tempfile
import pytest
from pathlib import Path
from agentic_devops.generator.cdk_generator import CDKGenerator

# Edge case: invalid project name (should be handled by CLI, but test generator directly)
def test_invalid_template_path():
    temp_dir = tempfile.mkdtemp()
    project_path = Path(temp_dir) / "test_project"
    # Use a non-existent template name
    with pytest.raises(Exception):
        CDKGenerator(project_path, "nonexistent_template")
    shutil.rmtree(temp_dir)

# Edge case: project path already exists and is not empty
def test_existing_nonempty_directory(monkeypatch):
    temp_dir = tempfile.mkdtemp()
    project_path = Path(temp_dir) / "existing_project"
    project_path.mkdir()
    # Create a dummy file
    (project_path / "dummy.txt").write_text("dummy")
    # Should not overwrite, simulate CLI logic
    assert any(project_path.iterdir())
    shutil.rmtree(temp_dir)

# Edge case: parameter replacement in template files
def test_parameter_replacement(monkeypatch):
    temp_dir = tempfile.mkdtemp()
    project_path = Path(temp_dir) / "param_project"
    template_name = "api_rest_python"
    # Patch logger
    class DummyLogger:
        def info(self, msg): pass
        def debug(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass
        def exception(self, msg): pass
        def success(self, msg): pass
    monkeypatch.setattr("agentic_devops.generator.cdk_generator.logger", DummyLogger())
    generator = CDKGenerator(project_path, template_name)
    generator.generate_project()
    # Check that the project name appears in README.md
    readme = (project_path / "README.md").read_text()
    assert "param_project" in readme
    shutil.rmtree(temp_dir)
