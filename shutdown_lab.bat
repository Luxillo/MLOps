@echo off
echo 🛑 Cierre del Laboratorio MLOps
echo ================================
echo.

echo 🔍 Terminando procesos MLflow...
taskkill /F /IM "mlflow.exe" >nul 2>&1
if %errorlevel% == 0 (
    echo    ✅ MLflow terminado
) else (
    echo    ℹ️  MLflow no estaba ejecutándose
)

echo.
echo 🔌 Liberando puertos...

REM Liberar puerto 5000 (MLflow UI)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
    if not errorlevel 1 echo    ✅ Puerto 5000 liberado
)

REM Liberar puerto 8081 (API del modelo)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8081 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
    if not errorlevel 1 echo    ✅ Puerto 8081 liberado
)

echo.
echo 🧹 Limpiando archivos temporales...
if exist __pycache__ (
    rmdir /s /q __pycache__ >nul 2>&1
    echo    ✅ Cache de Python eliminado
)

echo.
echo 🔄 Desactivando entorno virtual...
if defined VIRTUAL_ENV (
    echo    ✅ Entorno virtual detectado: %VIRTUAL_ENV%
    echo    💡 Ejecutando deactivate...
    call deactivate
) else (
    echo    ℹ️  No se detectó entorno virtual activo
)

echo.
echo ================================
echo ✅ ¡Laboratorio cerrado exitosamente!
echo.
echo 📋 Resumen de acciones:
echo    • Procesos MLflow terminados
echo    • Puertos 5000 y 8081 liberados  
echo    • Archivos temporales limpiados
echo    • Entorno virtual desactivado
echo.
echo 💡 Para reactivar el laboratorio:
echo    1. mlops_env\Scripts\activate
echo    2. mlflow ui
echo    3. python serve_model_local.py
echo.
echo 🎉 ¡Gracias por usar el laboratorio MLOps!
echo.
pause