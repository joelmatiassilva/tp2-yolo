#!/bin/bash

# Detener el script si ocurre un error
set -e

# Obtener el directorio donde está el script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "🚀 Iniciando configuración del entorno para Detector de Empanadas..."

# Verificar si uv está instalado
if ! command -v uv &> /dev/null; then
    echo "📦 'uv' no detectado. Instalando uv..."
    # Intentar instalar con pip si es posible, o instruir al usuario
    if command -v pip &> /dev/null; then
        pip install uv
    elif command -v pip3 &> /dev/null; then
        pip3 install uv
    else
        echo "❌ No se encontró pip ni uv. Por favor instala uv manualmente: https://github.com/astral-sh/uv"
        exit 1
    fi
else
    echo "✅ 'uv' detectado."
fi

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "🛠️ Creando entorno virtual con uv..."
    uv venv
else
    echo "ℹ️ El entorno virtual ya existe."
fi

# Activar el entorno para instalar dependencias
# Nota: uv pip install detecta el entorno virtual si está activo o si se usa --python
echo "📥 Instalando dependencias desde requirements.txt..."
uv pip install -r requirements.txt

echo "✅ ¡Configuración completada exitosamente!"
echo ""
echo "Para ejecutar la aplicación, usa los siguientes comandos:"
echo "  source .venv/bin/activate"
echo "  streamlit run app.py"

