# Agentic DevOps Assistant - Fase 1: Generador de CDK (Python)

¡Bienvenido al **Agentic DevOps Assistant**! Esta primera fase se enfoca en automatizar la creación de la estructura base de tus proyectos AWS CDK, permitiéndote empezar a construir tu infraestructura de manera más rápida y consistente.

Este asistente está diseñado para ser utilizado a través de una interfaz de línea de comandos (CLI) interactiva, utilizando **Python** como lenguaje principal tanto para el agente como para el código CDK que genera. Fomentamos el uso de las mejores prácticas de desarrollo en Python para asegurar la mantenibilidad y reproducibilidad de nuestro código.

---

## 🚀 Comencemos: Tu Primer Proyecto CDK con Asistencia

El objetivo de esta fase es generar el código CDK en Python para una aplicación común (ej. una API RESTful básica utilizando AWS Lambda y API Gateway).

### 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

1.  **Python 3.8+:** El asistente y el código CDK generado están desarrollados en Python.
2.  **AWS CLI:** Configurado con credenciales válidas para tu cuenta de AWS. Puedes seguir la [documentación oficial de AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) para configurarlo.
3.  **Git:** Para la gestión de versiones del código.
4.  **Docker (Opcional pero recomendado):** Para asegurar un entorno de desarrollo consistente y aislado.

### 🛠️ Configuración del Entorno de Desarrollo

Para asegurar un entorno limpio y reproducible, recomendamos enfáticamente el uso de **entornos virtuales de Python**.

1.  **Clonar el Repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_DEL_ASISTENTE>
    cd agentic_devops_assistant_project
    ```

2.  **Crear y Activar un Entorno Virtual (`.venv`):**
    Utilizaremos el módulo `venv` de Python para crear un entorno aislado.
    ```bash
    python -m venv .venv
    ```
    *   En **Linux/macOS**:
        ```bash
        source .venv/bin/activate
        ```
    *   En **Windows**:
        ```bash
        .venv\Scripts\activate
        ```
    Notarás que tu prompt de terminal cambiará para indicar que el entorno virtual está activo (ej. `(.venv) $`).

3.  **Instalar Dependencias:**
    Instala las dependencias del asistente, incluyendo el propio agente, usando `pip`. Es crucial hacerlo dentro del entorno virtual activado.
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Si el asistente se empaqueta como `setup.py`, la instalación podría ser `pip install -e .`)*

### 🚀 Usando el Asistente: El Comando Principal

El comando principal para interactuar con el asistente es `agentic-devops`. Asegúrate de que tu entorno virtual esté activado.

#### Generar un Nuevo Proyecto CDK (Python): `agentic-devops new`

Este comando iniciará un proceso interactivo para crear la estructura de tu proyecto CDK escrito en Python.

**Flujo del Comando:**

1.  **Solicitud de Nombre del Proyecto:**
    ```bash
    agentic-devops new
    ```
    El asistente te preguntará:
    `Por favor, introduce el nombre de tu nuevo proyecto CDK (ej. my-aws-python-api):`

2.  **Selección de la Pila Base (Stack):**
    Actualmente, el MLP soporta la siguiente pila:
    `Selecciona la pila base para tu proyecto:`
    `1. API RESTful (Python Lambda + API Gateway)`
    `2. Aplicación Web Estática (S3 + CloudFront)`
    `Introduce el número de tu elección:`

3.  **Confirmación y Generación:**
    Una vez que proporciones la información, el asistente:
    *   Creará una nueva carpeta con el nombre de tu proyecto.
    *   Generará la estructura de carpetas CDK en Python (ej. `app/`, `lib/`, `tests/`).
    *   Escribirá el código CDK base en Python.
    *   Configurará un archivo `requirements.txt` básico para las dependencias del proyecto CDK.
    *   Creará un repositorio Git inicial.
    *   (Próximamente en Fase 2) Configurará un pipeline básico de GitHub Actions.

    Verás mensajes indicando el progreso, por ejemplo:
    `[INFO] Creating project directory: my-aws-python-api`
    `[INFO] Generating CDK code for 'API RESTful (Python)' stack...`
    `[INFO] Initializing Git repository...`
    `[SUCCESS] CDK Project (Python) generated successfully!`

#### Opciones Adicionales (Próximamente)

*   `agentic-devops add-pipeline`: Para añadir un pipeline CI/CD a un proyecto CDK existente.
*   `agentic-devops init`: Para inicializar el asistente en un directorio existente.

### ⚙️ Lenguaje y Tecnologías

*   **Lenguaje Principal del Agente:** Python
*   **Lenguaje del Código CDK Generado:** Python
*   **Herramientas de Infraestructura:** AWS CDK (Python CDK)
*   **Control de Versiones:** Git
*   **Gestión de Dependencias de Python:** `venv` y `pip`
*   **Interacción:** GitHub API (para creación de repositorios)

### 📝 Estándares de Desarrollo

*   **Entornos Virtuales:** Siempre usa `.venv` para aislar dependencias.
*   **Gestión de Dependencias:** Usa `requirements.txt` para listar las dependencias del proyecto CDK y `requirements-dev.txt` (a crear en fases posteriores) para las dependencias de desarrollo/testing.
*   **Formato de Código:** Se recomienda el uso de herramientas como `Black` y `isort` para mantener un código limpio y consistente. Estas se integrarán en los pipelines de CI/CD.
*   **Linting y Análisis Estático:** Se utilizarán `Flake8` y `mypy` para asegurar la calidad del código Python.

### 🐞 Reportar un Problema

Si encuentras algún error o comportamiento inesperado, por favor, [crea un Issue en nuestro GitHub](https://github.com/your-org/agentic-devops-assistant/issues/new) (reemplaza la URL con la de tu repositorio real). Asegúrate de incluir detalles sobre tu entorno (Python, OS, versión del asistente) y los pasos para reproducir el problema.

---

**Gracias por usar el Agentic DevOps Assistant. ¡Estamos emocionados de ayudarte a acelerar tus flujos de trabajo DevOps con Python y sus mejores prácticas!**