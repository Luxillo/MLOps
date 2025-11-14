@echo off
echo 🚀 Configuración Automática MLOps Lab
echo =====================================
echo.

echo 📦 Actualizando pip...
python -m pip install --upgrade pip

echo.
echo 📋 Instalando dependencias desde requirements.txt...
python -m pip install -r requirements.txt

echo.
echo 🔍 Verificando instalación...
python verify_environment.py

echo.
echo ✅ Configuración completada
pause