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

        self.template_source_path = self.templates_base_dir / selected_stack # Usar variable 'selected_stack' definida en cli.py

        if not self.template_source_path.exists():
            raise AgentDevOpsError(f"No se encontró la plantilla '{stack_template_name}' en: {self.template_source_path}")

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
        Aplica parámetros específicos del proyecto a los archivos de la plantilla.
        En MLP, esto puede ser mínimo, pero se deja la estructura.
        """
        logger.debug("Aplicando parámetros a la plantilla...")
        # Ejemplo: Podríamos buscar y reemplazar el nombre del proyecto en los archivos.
        # Para esto, necesitamos el nombre real del proyecto, que viene de cli.py.
        # Esto requiere pasar el nombre del proyecto al constructor o tenerlo disponible.
        # Asumiendo que self.project_path.name contiene el nombre real.

        # Ejemplo: buscar y reemplazar en 'lib/api_rest_stack.py' y 'bin/app.py'
        # y en 'requirements.txt' si el nombre del paquete CDK dependiera de ello.
        logger.debug("Parámetros aplicados.")