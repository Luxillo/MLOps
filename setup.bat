@echo off
echo 🚀 Configuración Automática MLOps Lab
echo =====================================
echo.

REM Detectar comando Python
python --version >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_CMD=python
    echo 🐍 Usando: python
) else (
    python3 --version >nul 2>&1
    if %errorlevel% == 0 (
        set PYTHON_CMD=python3
        echo 🐍 Usando: python3
    ) else (
        echo ❌ Error: Python no encontrado
        pause
        exit /b 1
    )
)

echo 🔧 Creando entorno virtual...
%PYTHON_CMD% -m venv mlops_env

echo ⚡ Activando entorno virtual...
call mlops_env\Scripts\activate

echo 📦 Actualizando pip...
%PYTHON_CMD% -m pip install --upgrade pip

echo.
echo 📋 Instalando dependencias desde requirements.txt...
%PYTHON_CMD% -m pip install -r requirements.txt

echo.
echo 🔍 Verificando instalación...
python verify_environment.py

echo.
echo ✅ Configuración completada
pause