# Proyecto CDK: Web App Estática Generada

Este proyecto AWS CDK fue generado automáticamente por el Agentic DevOps Assistant. Contiene una pila básica para desplegar una aplicación web estática en S3 y servirla con CloudFront.

## Variables de entorno sugeridas

Puedes crear un archivo `.env` en la raíz del proyecto con variables como:

```
CDK_PROJECT_NAME=my-static-web-app
CDK_AWS_REGION=us-east-1
CDK_AWS_ACCOUNT_ID=123456789012
CDK_ENV_NAME=dev
```

## 🚀 Despliegue con AWS CDK

### 📋 Requisitos Previos

* Python 3.8+ y `pip`
* AWS CLI: Configurado y con credenciales válidas.
* AWS CDK CLI: Instalado globalmente (`npm install -g aws-cdk`).
* Git: Para control de versiones.
* Entorno Virtual: Recomendado (`python -m venv .venv`, luego `source .venv/bin/activate`).

### ⚙️ Instalación de Dependencias

Dentro de tu entorno virtual activado, instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```
