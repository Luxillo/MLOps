#!/usr/bin/env python3
"""
Task 4: Model Registry & Versioning - SOLUTION

This is the completed solution for Task 4.
All TODOs have been filled in with the correct MLflow API calls.

IMPORTANT: This solution uses modern MLflow aliases (2.9+) instead of deprecated stages.
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
df = pd.read_csv('/root/code/devops_metrics.csv')

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

    # SOLUTION for TODO 1: Log the trained model
    mlflow.sklearn.log_model(model, "model")

    # Store run ID for registration (outside the run block)
    run_id = run.info.run_id

# IMPORTANT: Model registration must happen OUTSIDE the run block
print("📦 Registering model to MLflow Registry...")

# Build model URI from the run we just completed
model_uri = f"runs:/{run_id}/model"

# SOLUTION for TODO 2: Register the model
registered_model = mlflow.register_model(
    model_uri,
    "DevOps-Response-Predictor"
)

model_name = registered_model.name
model_version = registered_model.version

print(f"   ✅ Model registered: {model_name} v{model_version}\n")

# SOLUTION for TODO 3: Set alias for the registered model
# Modern MLflow uses aliases instead of deprecated stages
client.set_registered_model_alias(
    model_name,
    "staging",
    model_version
)

print(f"   ✅ Model alias 'staging' set to v{model_version}\n")

print("🔄 Loading registered model for predictions...")

# Build model URI for loading from registry using alias
model_uri_registry = f"models:/{model_name}@staging"

# SOLUTION for TODO 4: Load the registered model
loaded_model = mlflow.pyfunc.load_model(model_uri_registry)

# Test the loaded model
sample_data = X_test.iloc[:3]
predictions = loaded_model.predict(sample_data)

print("   ✅ Model loaded successfully from registry!\n")
print("📊 Sample Predictions:")
for i, pred in enumerate(predictions):
    print(f"   Sample {i+1}: {pred:.2f} ms")

print()
print("=" * 60)
print("✅ Model Registry Setup Complete!")
print()
print("🌐 Next Steps:")
print("   1. Open MLflow UI (View Port → 5000)")
print("   2. Click 'Models' tab at the top")
print("   3. See 'DevOps-Response-Predictor' model")
print("   4. View version, aliases, and metadata!")
print()
print("🚀 Production Workflow:")
print("   dev → staging → production")
print("    ↓       ↓          ↓")
print("   Test  Validate    Serve")
print("=" * 60)

# Create success marker
os.makedirs('/root/markers', exist_ok=True)
with open('/root/markers/task4_registry_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ Task 4 Complete!")
print("🎉 All MLflow fundamentals mastered!")
