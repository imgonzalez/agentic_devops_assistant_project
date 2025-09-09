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
@click.option('--github', is_flag=True, help='Crear y subir el proyecto a un repositorio GitHub (requiere GITHUB_TOKEN)')
def new(project_name: str, stack_type: str, github: bool):
    import re
    # Validate project name (alphanumeric, dashes, underscores, no spaces)
    if not re.match(r'^[a-zA-Z0-9_-]+$', project_name):
        logger.error("El nombre del proyecto solo puede contener letras, números, guiones y guiones bajos, sin espacios.")
        return
    if len(project_name) < 3:
        logger.error("El nombre del proyecto debe tener al menos 3 caracteres.")
        return
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
            if not project_path.is_dir():
                logger.error(f"'{project_name}' existe pero no es un directorio.")
                return
            if any(project_path.iterdir()):
                logger.error(f"El directorio '{project_name}' ya existe y no está vacío. Aborta para evitar sobrescribir archivos.")
                return
            logger.warning(f"El directorio '{project_name}' ya existe y está vacío. Se usará para el nuevo proyecto.")
        else:
            project_path.mkdir()
            logger.info(f"Directorio del proyecto creado: {project_name}")

        # Instanciar generador
        generator = CDKGenerator(project_path, selected_stack)
        generator.generate_project()

        # Inicializar Git
        import subprocess
        if not (project_path / ".git").exists():
            logger.info("Inicializando repositorio Git...")
            subprocess.run(["git", "init"], cwd=project_path)
            subprocess.run(["git", "add", "."], cwd=project_path)
            subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path)
            logger.info("Repositorio Git inicializado.")
        else:
            logger.info("Directorio ya es un repositorio Git.")

        # GitHub integration if requested
        if github:
            try:
                from agentic_devops.generator.github_client import GitHubClient
                logger.info("Creando repositorio en GitHub...")
                gh_client = GitHubClient()
                repo_url = gh_client.create_repo(project_name, private=True)
                logger.info(f"Repositorio GitHub creado: {repo_url}")
                subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=project_path)
                subprocess.run(["git", "push", "-u", "origin", "master"], cwd=project_path)
                logger.success("Proyecto subido a GitHub exitosamente.")
            except Exception as e:
                logger.error(f"Error al crear o subir a GitHub: {e}")

        logger.success(f"¡Proyecto CDK '{project_name}' generado exitosamente!")
        logger.info("Siguientes pasos:")
        logger.info(f"1. Navega a la carpeta del proyecto: cd {project_name}")
        logger.info("2. Activa el entorno virtual: source .venv/bin/activate (Linux/macOS) o .venv\\Scripts\\activate (Windows)")
        logger.info("3. Instala las dependencias del proyecto: pip install -r requirements.txt")
        logger.info("4. Explora la estructura generada y el código CDK.")
        logger.info("5. Considera añadir tu repositorio a GitHub y configurar el pipeline (Fase 2)." if not github else "5. El repositorio ya fue creado y subido a GitHub.")

    except AgentDevOpsError as e:
        logger.error(f"Error durante la generación del proyecto: {e}")
    except Exception as e:
        logger.exception(f"Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    cli()