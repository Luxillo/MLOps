#!/bin/bash

echo "🛑 Cierre del Laboratorio MLOps"
echo "================================"
echo

echo "🔍 Terminando procesos MLflow..."
pkill -f "mlflow ui" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   ✅ MLflow UI terminado"
else
    echo "   ℹ️  MLflow UI no estaba ejecutándose"
fi

pkill -f "mlflow.*serve" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   ✅ MLflow serve terminado"
else
    echo "   ℹ️  MLflow serve no estaba ejecutándose"
fi

echo
echo "🔌 Liberando puertos..."

# Liberar puerto 5000 (MLflow UI)
PID_5000=$(lsof -ti:5000 2>/dev/null)
if [ ! -z "$PID_5000" ]; then
    kill -9 $PID_5000 2>/dev/null
    echo "   ✅ Puerto 5000 liberado"
else
    echo "   ℹ️  Puerto 5000 ya está libre"
fi

# Liberar puerto 8081 (API del modelo)
PID_8081=$(lsof -ti:8081 2>/dev/null)
if [ ! -z "$PID_8081" ]; then
    kill -9 $PID_8081 2>/dev/null
    echo "   ✅ Puerto 8081 liberado"
else
    echo "   ℹ️  Puerto 8081 ya está libre"
fi

echo
echo "🧹 Limpiando archivos temporales..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   ✅ Archivos temporales eliminados"
else
    echo "   ℹ️  No se encontraron archivos temporales"
fi

echo
echo "🔄 Desactivando entorno virtual..."
if [ ! -z "$VIRTUAL_ENV" ]; then
    echo "   ✅ Entorno virtual detectado: $VIRTUAL_ENV"
    echo "   💡 Ejecuta 'deactivate' para desactivar"
else
    echo "   ℹ️  No se detectó entorno virtual activo"
fi

echo
echo "================================"
echo "✅ ¡Laboratorio cerrado exitosamente!"
echo
echo "📋 Resumen de acciones:"
echo "   • Procesos MLflow terminados"
echo "   • Puertos 5000 y 8081 liberados"
echo "   • Archivos temporales limpiados"
echo
echo "💡 Para reactivar el laboratorio:"
echo "   1. source mlops_env/bin/activate"
echo "   2. mlflow ui"
echo "   3. python serve_model_local.py"
echo
echo "🎉 ¡Gracias por usar el laboratorio MLOps!"