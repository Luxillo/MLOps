#!/bin/bash
echo "🚀 Configuración Automática MLOps Lab"
echo "====================================="
echo

echo "📦 Actualizando pip..."
python3 -m pip install --upgrade pip

echo
echo "📋 Instalando dependencias desde requirements.txt..."
python3 -m pip install -r requirements.txt

echo
echo "🔍 Verificando instalación..."
python3 verify_environment.py

echo
echo "✅ Configuración completada"