#!/usr/bin/env python3
"""
Tarea 2: Ajuste de Hiperparámetros con Seguimiento MLflow

En esta tarea, compararás diferentes configuraciones de Random Forest
registrando sistemáticamente hiperparámetros y métricas.

Objetivos de Aprendizaje:
- Registrar hiperparámetros individuales
- Registrar múltiples parámetros en lote
- Registrar y comparar métricas entre ejecuciones
- Usar etiquetas para organizar experimentos
"""

import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import os

# Establecer experimento MLflow
mlflow.set_experiment("DevOps-Response-Time-Prediction")

# Cargar dataset
print("📊 Cargando dataset de métricas DevOps...")
df = pd.read_csv('devops_metrics.csv')

X = df.drop('response_time_ms', axis=1)
y = df['response_time_ms']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"🔬 Ajuste de Hiperparámetros: Random Forest")
print(f"   Probando diferentes valores de max_depth...\n")

# Probar diferentes valores de max_depth
depths = [5, 10, 15]

for depth in depths:
    with mlflow.start_run(run_name=f"RandomForest_depth_{depth}"):
        print(f"🌳 Training Random Forest (max_depth={depth})...")

        # TODO 1 (Line 49): Log the max_depth parameter
        # Hint: mlflow.log_param("max_depth", depth)
        mlflow.log_param(___, depth)  # FILL IN FIRST ARGUMENT

        # Train model
        model = RandomForestRegressor(
            max_depth=depth,
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate metrics
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        # TODO 2 (Line 71): Batch log multiple parameters at once
        # Hint: mlflow.log_params({"n_estimators": 100, "random_state": 42})
        # This is more efficient than logging parameters one by one
        mlflow.log_params({
            "": 100,  # FILL IN PARAMETER NAME
            "": 42    # FILL IN PARAMETER NAME
        })

        # TODO 3 (Line 78): Log the R² score metric
        # Hint: mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("", r2)  # FILL IN FIRST ARGUMENT

        # Log additional metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)

        # TODO 4 (Line 87): Tag this run with the model family
        # Hint: mlflow.set_tag("model_family", "RandomForest")
        # Tags help organize and filter experiments
        mlflow.set_tag("", "")  # FILL IN BOTH ARGUMENTS

        print(f"   ✅ RMSE: {rmse:.2f}")
        print(f"   ✅ R²: {r2:.4f}")
        print(f"   ✅ MAE: {mae:.2f}\n")

print("=" * 60)
print("✅ ¡Ajuste de hiperparámetros completado!")
print()
print("🌐 Próximos pasos:")
print(" 1. Abra la interfaz de usuario de MLflow (Ventana → 5000)")
print(" 2. Haga clic en 'DevOps-Response-Time-Prediction'")
print(" 3. Marque las casillas junto a las 3 ejecuciones de RandomForest")
print(" 4. Haga clic en el botón 'Comparar' en la parte superior")
print(" 5. Ordene por r2_score para encontrar la mejor configuración!")
print("=" * 60)

# Create success marker
os.makedirs('markers', exist_ok=True)
with open('markers/task2_tuning_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ Tarea 2 completada: ¡Ajuste de hiperparámetros realizado!")
