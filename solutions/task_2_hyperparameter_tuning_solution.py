#!/usr/bin/env python3
"""
Task 2: Hyperparameter Tuning with MLflow Tracking - SOLUTION

This is the completed solution for Task 2.
All TODOs have been filled in with the correct MLflow API calls.
"""

import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
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

print(f"🔬 Hyperparameter Tuning: Random Forest")
print(f"   Testing different max_depth values...\n")

# Test different max_depth values
depths = [5, 10, 15]

for depth in depths:
    with mlflow.start_run(run_name=f"RandomForest_depth_{depth}"):
        print(f"🌳 Training Random Forest (max_depth={depth})...")

        # SOLUTION for TODO 1: Log the max_depth parameter
        mlflow.log_param("max_depth", depth)

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

        # SOLUTION for TODO 2: Batch log multiple parameters at once
        mlflow.log_params({
            "n_estimators": 100,
            "random_state": 42
        })

        # SOLUTION for TODO 3: Log the R² score metric
        mlflow.log_metric("r2_score", r2)

        # Log additional metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)

        # SOLUTION for TODO 4: Tag this run with the model family
        mlflow.set_tag("model_family", "RandomForest")

        print(f"   ✅ RMSE: {rmse:.2f}")
        print(f"   ✅ R²: {r2:.4f}")
        print(f"   ✅ MAE: {mae:.2f}\n")

print("=" * 60)
print("✅ Hyperparameter tuning complete!")
print()
print("🌐 Next Steps:")
print("   1. Open MLflow UI (View Port → 5000)")
print("   2. Click 'Compare' button (select all 3 runs)")
print("   3. View parallel coordinates plot")
print("   4. Identify which max_depth performed best!")
print("=" * 60)

# Create success marker
os.makedirs('/root/markers', exist_ok=True)
with open('/root/markers/task2_tuning_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ Task 2 Complete: Hyperparameter Tuning Tracked!")
