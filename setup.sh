#!/bin/bash
echo "🚀 Configuración Automática MLOps Lab"
echo "====================================="
echo

# Detectar comando Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python no encontrado"
    exit 1
fi

echo "🐍 Usando: $PYTHON_CMD"

echo "🔧 Creando entorno virtual..."
$PYTHON_CMD -m venv mlops_env

echo "⚡ Activando entorno virtual..."
source mlops_env/bin/activate

echo "📦 Actualizando pip..."
$PYTHON_CMD -m pip install --upgrade pip

echo
echo "📋 Instalando dependencias desde requirements.txt..."
$PYTHON_CMD -m pip install -r requirements.txt

echo
echo "🔍 Verificando instalación..."
python3 verify_environment.py

echo
echo "✅ Configuración completada"