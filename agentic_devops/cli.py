import click
import os
import shutil
from pathlib import Path

# Importar módulos internos
from agentic_devops.generator.cdk_generator import CDKGenerator
from agentic_devops.generator.github_client import GitHubClient
from agentic_devops.utils.logger import setup_logging
from agentic_devops.utils.exceptions import AgentDevOpsError

# Configurar logger
logger = setup_logging(__name__)

# Comando principal para la CLI
@click.group()
def cli():
    """Agentic DevOps Assistant CLI. Automatiza la creación de proyectos CDK."""
    pass

# Comando 'new' para crear un nuevo proyecto
@cli.command()
@click.option('--project-name', prompt='Por favor, introduce el nombre de tu nuevo proyecto CDK (ej. my-aws-python-api)', type=str)
@click.option('--stack-type', prompt='Selecciona la pila base para tu proyecto:\n1. API RESTful (Python Lambda + API Gateway)\n2. Aplicación Web Estática (S3 + CloudFront)\nIntroduce el número de tu elección:', type=click.Choice(['1', '2']), default='1')
def new(project_name: str, stack_type: str):
    """Genera una nueva estructura de proyecto AWS CDK."""
    logger.info(f"Iniciando la creación del proyecto CDK: {project_name}")

    # Determinar el tipo de stack y la plantilla a usar
    stack_mapping = {
        '1': 'api_rest_python',
        '2': 'static_web_app',
    }
    selected_stack = stack_mapping.get(stack_type)
    if not selected_stack:
        logger.error("Tipo de stack seleccionado no válido.")
        return

    try:
        # Crear cliente de GitHub (simplificado para MLP: asume que el usuario configuro credenciales o variables de entorno)
        # En MLP, podemos pedir la URL del repo o el token, o solo init git localmente.
        # Por ahora, nos enfocaremos en la generación local y git init.
        # github_token = os.environ.get("GITHUB_TOKEN")
        # github_client = GitHubClient(github_token)

        # Crear directorio del proyecto
        project_path = Path(project_name)
        if project_path.exists():
            logger.warning(f"El directorio '{project_name}' ya existe. Se añadirá el contenido dentro si es posible o se dará error.")
            # Para MLP, podríamos preguntar si se sobrescribe o se aborta.
            # Aquí asumimos que creamos si no existe, o fallamos si hay conflicto.
            if not project_path.is_dir():
                raise AgentDevOpsError(f"'{project_name}' existe pero no es un directorio.")
        else:
            project_path.mkdir()
            logger.info(f"Directorio del proyecto creado: {project_name}")

        # Instanciar generador
        generator = CDKGenerator(project_path, selected_stack)
        generator.generate_project()

        # Inicializar Git
        if not (project_path / ".git").exists():
            # Ejecutar git init si el directorio está vacío o no es un repo git
            # En un sistema real, esto usaría subprocess.run(['git', 'init'], cwd=project_path)
            logger.info("Inicializando repositorio Git...")
            # Simulación: Crear un archivo .git/ para indicar que está inicializado
            Path(project_path / ".git").mkdir(exist_ok=True)
            logger.info("Repositorio Git inicializado (simulado).")
        else:
            logger.info("Directorio ya es un repositorio Git.")

        logger.success(f"¡Proyecto CDK '{project_name}' generado exitosamente!")
        logger.info("Siguientes pasos:")
        logger.info(f"1. Navega a la carpeta del proyecto: cd {project_name}")
        logger.info("2. Activa el entorno virtual: source .venv/bin/activate (Linux/macOS) o .venv\\Scripts\\activate (Windows)")
        logger.info("3. Instala las dependencias del proyecto: pip install -r requirements.txt")
        logger.info("4. Explora la estructura generada y el código CDK.")
        logger.info("5. Considera añadir tu repositorio a GitHub y configurar el pipeline (Fase 2).")

    except AgentDevOpsError as e:
        logger.error(f"Error durante la generación del proyecto: {e}")
    except Exception as e:
        logger.exception(f"Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    cli()