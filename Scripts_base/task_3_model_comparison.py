#!/usr/bin/env python3
"""
Task 3: Model Comparison & Selection

In this task, you'll train multiple model types and systematically
compare their performance to select the best one for production.

Learning Objectives:
- Compare different model architectures
- Log multiple metrics at once
- Save trained models as artifacts
- Use MLflow UI to identify the best model
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
df = pd.read_csv('devops_metrics.csv')

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

        # TODO 1 (Line 54): Log the model name as a parameter
        # Hint: mlflow.log_param("model_name", model_name)
        mlflow.log_param("model_name", ___)  # FILL IN SECOND ARGUMENT

        # Train model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate all metrics
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        # TODO 2 (Line 70): Log all metrics at once
        # Hint: mlflow.log_metrics({"rmse": rmse, "r2_score": r2, "mae": mae})
        # This is the most efficient way to log multiple metrics
        mlflow.log_metrics({
            ___: rmse,  # FILL IN METRIC NAME
            ___: r2,    # FILL IN METRIC NAME
            ___: mae    # FILL IN METRIC NAME
        })

        # TODO 3 (Line 79): Log the trained model as an artifact
        # Hint: mlflow.sklearn.log_model(model, "model")
        # This saves the model so it can be loaded and used later
        mlflow.sklearn.log_model(___, "model")  # FILL IN FIRST ARGUMENT

        # Set model type tag
        mlflow.set_tag("model_type", model_name)

        print(f"   ✅ RMSE: {rmse:.2f}")
        print(f"   ✅ R²: {r2:.4f}")
        print(f"   ✅ MAE: {mae:.2f}")
        print(f"   ✅ Model saved\n")

print("=" * 60)
print("✅ Model comparison complete!")
print()
print("🌐 Next Steps:")
print("   1. Open MLflow UI (View Port → 5000)")
print("   2. Sort runs by 'r2_score' (descending)")
print("   3. Click on the winning model run")
print("   4. See the saved model artifact!")
print()
print("💡 Typical Results:")
print("   - LinearRegression:    R² ≈ 0.85")
print("   - RandomForest:        R² ≈ 0.92")
print("   - GradientBoosting:    R² ≈ 0.94 ← Usually wins!")
print("=" * 60)

# Create success marker
os.makedirs('markers', exist_ok=True)
with open('markers/task3_comparison_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("✅ Task 3 Complete!")
