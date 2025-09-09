#!/bin/bash
# Script simple para activar el entorno virtual en Linux/macOS

echo "Activando entorno virtual .venv..."
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "Entorno virtual activado."
else
    echo "Error: No se encontró el script 'activate' en .venv/bin/"
    echo "Asegúrate de haber creado el entorno virtual: python -m venv .venv"
fi