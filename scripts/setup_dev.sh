#!/bin/bash
# Script para configurar el entorno de desarrollo

echo "Configurando entorno de desarrollo..."

# 1. Crear y activar entorno virtual
if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual..."
    python -m venv .venv
    if [ $? -ne 0 ]; then echo "Error al crear el entorno virtual. Abortando."; exit 1; fi
fi

# Activar entorno virtual (ajustar según SO)
if [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
    source .venv/bin/activate
elif [ -n "$OS" ] && [[ "$OS" == *"Windows"* ]]; then
    .venv\Scripts\activate
else
    echo "Sistema operativo no reconocido para activación automática de venv. Actívalo manualmente."
fi

# 2. Instalar dependencias del asistente
echo "Instalando dependencias del asistente..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then echo "Error al instalar dependencias. Abortando."; exit 1; fi
else
    echo "Advertencia: No se encontró requirements.txt. Instala las dependencias manualmente."
fi

# 3. (Opcional) Instalar dependencias de desarrollo
# if [ -f "requirements-dev.txt" ]; then
#     echo "Instalando dependencias de desarrollo..."
#     pip install -r requirements-dev.txt
#     if [ $? -ne 0 ]; then echo "Error al instalar dependencias de desarrollo."; fi
# fi

echo "Entorno de desarrollo configurado exitosamente."
echo "Ejecuta 'agentic-devops --help' para ver los comandos disponibles."