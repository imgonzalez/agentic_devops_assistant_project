#!/usr/bin/env python3
import os
import sys

from aws_cdk import App, Environment
# from constructs import Construct # No es estrictamente necesario importar si no se usa directamente

# Importa tu stack desde el directorio 'lib'
from api_rest_stack import ApiRestStack

# --- Configuración del proyecto ---
# Estos valores podrían ser reemplazados dinámicamente por el generador
# o cargados de un archivo de configuración.
# Por simplicidad en MLP, se usan valores hardcoded o tomados del entorno.
PROJECT_NAME = os.environ.get("CDK_PROJECT_NAME", "my-generated-api")
AWS_REGION = os.environ.get("CDK_AWS_REGION", "us-east-1")
AWS_ACCOUNT_ID = os.environ.get("CDK_AWS_ACCOUNT_ID", "123456789012") # Usar un ID placeholder

# Puedes añadir un nombre de entorno o usar el nombre del proyecto
ENV_NAME = os.environ.get("CDK_ENV_NAME", PROJECT_NAME)
# ---------------------------------

app = App()

# Define el entorno de despliegue
env_config = Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION)

# Crea la instancia de la pila
ApiRestStack(app, f"{ENV_NAME}-api-stack", 
             env=env_config,
             description="Stack de API RESTful generado por Agentic DevOps Assistant")

# Opcional: Añadir tags a todos los recursos
# tags = {"CreatedBy": "AgenticDevOpsAssistant", "Environment": ENV_NAME}
# tags.forEach(lambda tag, value: Core.Tags.of(app).add(tag, value))

app.synth()