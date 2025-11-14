#!/usr/bin/env python3
"""
Task 3: Model Comparison & Selection - SOLUTION

This is the completed solution for Task 3.
All TODOs have been filled in with the correct MLflow API calls.
"""

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import os

# Set MLflow experiment
mlflow.set_experiment("DevOps-Response-Time-Prediction")

# Load dataset
print("📊 Loading DevOps metrics dataset...")
df = pd.read_csv('/root/code/devops_metrics.csv')

X = df.drop('response_time_ms', axis=1)
y = df['response_time_ms']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define models to compare
models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(max_depth=15, n_estimators=100, random_state=42, n_jobs=-1),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
}

print(f"🔬 Model Comparison: Testing {len(models)} different algorithms\n")

for model_name, model in models.items():
    with mlflow.start_run(run_name=f"Model_Comparison_{model_name}"):
        print(f"🤖 Training {model_name}...")

        # SOLUTION for TODO 1: Log the model name as a parameter
        mlflow.log_param("model_name", model_name)

        # Train model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate all metrics
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        # SOLUTION for TODO 2: Log all metrics at once
        mlflow.log_metrics({
            "rmse": rmse,
            "r2_score": r2,
            "mae": mae
        })

        # SOLUTION for TODO 3: Log the trained model as an artifact
        mlflow.sklearn.log_model(model, "model")

        # Set model type tag
        mlflow.set_tag("model_type", model_name)

        print(f"   ✅ RMSE: {rmse:.2f}")
        print(f"   ✅ R²: {r2:.4f}")
        print(f"   ✅ MAE: {mae:.2f}\n")

print("=" * 60)
print("✅ Model comparison complete!")
print()
print("🌐 Next Steps:")
print("   1. Open MLflow UI (View Port → 5000)")
print("   2. Sort runs by R² score (descending)")
print("   3. Identify the winning model!")
print("   4. Click on best run → 'Artifacts' → See saved model")
print()
print("🎯 Expected Winner: GradientBoosting (R² ≈ 0.94)")
print("=" * 60)

# Create success marker
os.makedirs('/root/markers', exist_ok=True)
with open('/root/markers/task3_comparison_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ Task 3 Complete: Model Comparison Tracked!")
