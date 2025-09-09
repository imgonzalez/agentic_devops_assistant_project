import os
import shutil
from pathlib import Path
import logging
import json

from agentic_devops.utils.exceptions import AgentDevOpsError
from agentic_devops.utils.logger import setup_logging

logger = setup_logging(__name__)

class CDKGenerator:
    def __init__(self, project_path: Path, stack_template_name: str):
        self.project_path = project_path
        self.stack_template_name = stack_template_name
        self.templates_base_dir = Path(__file__).resolve().parent.parent.parent / "cdk_templates"

        if not self.templates_base_dir.exists():
            raise AgentDevOpsError(f"No se encontró el directorio de plantillas en: {self.templates_base_dir}")


        self.template_source_path = self.templates_base_dir / self.stack_template_name
        if not self.template_source_path.exists():
            raise AgentDevOpsError(f"No se encontró la plantilla '{self.stack_template_name}' en: {self.template_source_path}")

    def generate_project(self):
        logger.info(f"Copiando plantilla '{self.stack_template_name}' a '{self.project_path}'")
        try:
            shutil.copytree(self.template_source_path, self.project_path, dirs_exist_ok=True)
            logger.info("Plantilla copiada exitosamente.")

            # Lógica de parametrización (para MLP, la plantilla ya está semi-configurada)
            # Aquí se podría reemplazar placeholders en archivos o generar requirements.txt dinámicamente
            # Por ejemplo, si la plantilla tuviera un archivo placeholder.txt con "{{ PROJECT_NAME }}",
            # se leería aquí y se reemplazaría.
            self._apply_template_params()

        except Exception as e:
            logger.exception(f"Error al copiar la plantilla: {e}")
            raise AgentDevOpsError(f"Error al copiar la plantilla: {e}")

    def _apply_template_params(self):
        """
        Busca y reemplaza placeholders en los archivos de la plantilla con valores del proyecto.
        """
        logger.debug("Aplicando parámetros a la plantilla...")
        replacements = {
            "{{ PROJECT_NAME }}": self.project_path.name,
            "{{ AWS_REGION }}": os.environ.get("CDK_AWS_REGION", "us-east-1"),
            "{{ AWS_ACCOUNT_ID }}": os.environ.get("CDK_AWS_ACCOUNT_ID", "123456789012"),
            "{{ ENV_NAME }}": os.environ.get("CDK_ENV_NAME", self.project_path.name),
        }
        # Archivos a parametrizar
        files_to_edit = [
            self.project_path / "bin/app.py",
            self.project_path / "lib/api_rest_stack.py",
            self.project_path / "requirements.txt",
        ]
        # Ensure README.md exists
        readme_path = self.project_path / "README.md"
        if not readme_path.exists():
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {self.project_path.name}\n\nProyecto generado por Agentic DevOps Assistant.\n\n## Uso\n\n1. Crea y activa un entorno virtual:\n   ```bash\n   python -m venv .venv\n   source .venv/bin/activate\n   ```\n2. Instala dependencias:\n   ```bash\n   pip install -r requirements.txt\n   ```\n3. Despliega con AWS CDK:\n   ```bash\n   cdk synth\n   cdk deploy\n   ```\n")
        files_to_edit.append(readme_path)
        for file_path in files_to_edit:
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                for k, v in replacements.items():
                    content = content.replace(k, v)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
        logger.debug("Parámetros aplicados.")