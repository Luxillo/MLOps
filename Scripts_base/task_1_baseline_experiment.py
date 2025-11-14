#!/usr/bin/env python3
"""
Tarea 1: Seguimiento de Experimento Base con MLflow

En esta tarea, rastrearás tu primer experimento de aprendizaje automático usando MLflow.
Entrenarás un modelo simple de Regresión Lineal y registrarás sus parámetros y métricas.

Objetivos de Aprendizaje:
- Establecer un nombre de experimento MLflow
- Iniciar una ejecución MLflow
- Registrar parámetros del modelo
- Registrar métricas de evaluación
"""

import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import os

# TODO 1 (Línea 26): Establecer el nombre del experimento MLflow
# Pista: mlflow.set_experiment("DevOps-Response-Time-Prediction")
# Esto agrupa todas tus ejecuciones bajo un experimento en la UI de MLflow
mlflow._  # REEMPLAZA ESTA LÍNEA

# Cargar el dataset
print("📊 Cargando dataset de métricas DevOps...")
df = pd.read_csv('devops_metrics.csv')
print(f"✅ Dataset cargado: {len(df)} muestras, {len(df.columns)} características")

# Preparar características y objetivo
X = df.drop('response_time_ms', axis=1)
y = df['response_time_ms']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"📈 Conjunto de entrenamiento: {len(X_train)} muestras")
print(f"📉 Conjunto de prueba: {len(X_test)} muestras")
print()

# TODO 2 (Línea 49): Iniciar una ejecución MLflow
# Pista: with mlflow.start_run():
# Este administrador de contexto rastrea todo lo que sucede dentro
with mlflow._():  # COMPLETA ESTA LÍNEA
    print("🔬 Entrenando modelo de Regresión Lineal...")

    # Entrenar el modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Hacer predicciones
    y_pred = model.predict(X_test)

    # Calcular métricas
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print("📊 Rendimiento del Modelo:")
    print(f"   RMSE: {rmse:.2f}")
    print(f"   Puntuación R²: {r2:.4f}")
    print(f"   MAE: {mae:.2f}")
    print()

    # TODO 3 (Línea 73): Registrar el parámetro tipo de modelo
    # Pista: mlflow.log_param("model_type", "LinearRegression")
    # Los parámetros son entradas a tu proceso de entrenamiento
    mlflow.log_param(___,___)  # COMPLETA AMBOS ARGUMENTOS

    # Registrar parámetro adicional
    mlflow.log_param("random_state", 42)

    # TODO 4 (Línea 81): Registrar la métrica RMSE
    # Pista: mlflow.log_metric("rmse", rmse)
    # Las métricas son salidas que miden el rendimiento del modelo
    mlflow.log_metric(__, rmse)  # COMPLETA AMBOS ARGUMENTOS

    # Registrar métricas adicionales
    mlflow.log_metric("r2_score", r2)
    mlflow.log_metric("mae", mae)

    print("✅ Parámetros y métricas del modelo registrados en MLflow")
    print()
    print("🌐 Siguiente Paso:")
    print("   1. Abrir UI de MLflow (View Port → 5000)")
    print("   2. Hacer clic en el experimento 'DevOps-Response-Time-Prediction'")
    print("   3. ¡Ver tus parámetros y métricas registrados!")

# Crear marcador de éxito
os.makedirs('markers', exist_ok=True)
with open('markers/task1_baseline_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ ¡Tarea 1 Completada!")
print("=" * 60)
