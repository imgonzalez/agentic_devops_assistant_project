#!/usr/bin/env python3
import os
from aws_cdk import App, Environment
from lib.static_web_stack import StaticWebStack

PROJECT_NAME = os.environ.get("CDK_PROJECT_NAME", "my-static-web-app")
AWS_REGION = os.environ.get("CDK_AWS_REGION", "us-east-1")
AWS_ACCOUNT_ID = os.environ.get("CDK_AWS_ACCOUNT_ID", "123456789012")
ENV_NAME = os.environ.get("CDK_ENV_NAME", PROJECT_NAME)

app = App()
env_config = Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION)
StaticWebStack(app, f"{ENV_NAME}-staticweb-stack", env=env_config, description="Stack de Web App Estática generado por Agentic DevOps Assistant")
app.synth()
