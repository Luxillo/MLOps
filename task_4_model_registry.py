#!/usr/bin/env python3
"""
Task 4: Model Registry & Versioning

In this task, you'll register your trained model in MLflow's Model Registry
for production deployment with version control.

Learning Objectives:
- Register a trained model
- Assign model versions
- Set model aliases for deployment stages
- Load registered models for deployment
"""

import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import os

# Set MLflow experiment
mlflow.set_experiment("DevOps-Response-Time-Prediction")

# Initialize MLflow client for registry operations
client = MlflowClient()

# Load dataset
print("📊 Loading DevOps metrics dataset...")
df = pd.read_csv('devops_metrics.csv')

X = df.drop('response_time_ms', axis=1)
y = df['response_time_ms']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("🚀 Task 4: Model Registry & Production Deployment\n")

# Train the best model from Task 3
with mlflow.start_run(run_name="Production_Candidate_GradientBoosting") as run:
    print("🤖 Training Gradient Boosting model...")

    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # Log parameters and metrics
    mlflow.log_param("model_type", "GradientBoostingRegressor")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2_score", r2)

    print(f"   ✅ Model trained: RMSE={rmse:.2f}, R²={r2:.4f}\n")

    # TODO 1 (Line 67): Log the trained model
    # Hint: mlflow.sklearn.log_model(model, "model")
    # This saves the model in the current run
    mlflow.sklearn.log_model(, "")  # FILL IN BOTH ARGUMENTS

    # Store run ID for registration (outside the run block)
    run_id = run.info.run_id

# IMPORTANT: Model registration must happen OUTSIDE the run block
print("📦 Registering model to MLflow Registry...")

# Build model URI from the run we just completed
model_uri = f"runs:/{run_id}/model"

# TODO 2 (Line 81): Register the model
# Hint: mlflow.register_model(model_uri, "DevOps-Response-Predictor")
# This creates a new registered model (or new version if it exists)
registered_model = mlflow.register_model(
    model_uri,  # FILL IN: model URI
    ""   # FILL IN: model name (e.g., "DevOps-Response-Predictor")
)

model_name = registered_model.name
model_version = registered_model.version

print(f"   ✅ Model registered: {model_name} v{model_version}\n")

# TODO 3 (Line 94): Set alias for the registered model
# Hint: client.set_registered_model_alias(model_name, "staging", model_version)
# Modern MLflow uses aliases instead of stages (staging, production, champion, etc.)
client.set_registered_model_alias(
    ,  # FILL IN: model name
    ___,  # FILL IN: alias name (e.g., "staging")
     ____  # FILL IN: model version
)

print(f"   ✅ Model alias 'staging' set to v{model_version}\n")

print("🔄 Loading registered model for predictions...")

# Build model URI for loading from registry using alias
model_uri_registry = f"models:/{model_name}@staging"

# TODO 4 (Line 110): Load the registered model
# Hint: mlflow.pyfunc.load_model(model_uri_registry)
# This loads the model from the registry for making predictions
loaded_model = mlflow.pyfunc.load_model(___)  # FILL IN ARGUMENT

# Test the loaded model
sample_data = X_test.iloc[:3]
predictions = loaded_model.predict(sample_data)

print("   ✅ Model loaded successfully from registry!\n")
print("📊 Sample Predictions:")
for i, pred in enumerate(predictions):
    print(f"   Sample {i+1}: {pred:.2f} ms")

print()
print("=" * 60)
print("✅ ¡Configuración del registro de modelos completada!")
print()
print("🌐 Próximos pasos:")
print(" 1. Abra la interfaz de usuario de MLflow (Ventana → 5000)")
print(" 2. Haga clic en la pestaña 'Modelos' en la parte superior")
print(" 3. Vea el modelo 'DevOps-Response-Predictor'")
print(" 4. Vea la versión, los alias y los metadatos!")
print()
print("🚀 Flujo de trabajo de producción:")
print(" desarrollo → pruebas → producción")
print(" ↓ ↓ ↓")
print(" Probar Validar Servir")
print("=" * 60)

# Create success marker
os.makedirs('/root/markers', exist_ok=True)
with open('/root/markers/task4_registry_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ ¡Tarea 4 completada!")
print("🎉 ¡Todos los fundamentos de MLflow dominados!")
print()
print("🧪 ¿Quieres probar tu modelo como API?")
print("   → Ve al directorio 'test/' y sigue la guía")
print("   → Ejecuta: cd test && python test_model_deployment.py")