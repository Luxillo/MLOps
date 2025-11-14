#!/usr/bin/env python3
"""
Task 1: Baseline Experiment Tracking with MLflow - SOLUTION

This is the completed solution for Task 1.
All TODOs have been filled in with the correct MLflow API calls.
"""

import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import os

# SOLUTION for TODO 1: Set the MLflow experiment name
mlflow.set_experiment("DevOps-Response-Time-Prediction")

# Load the dataset
print("📊 Loading DevOps metrics dataset...")
df = pd.read_csv('/root/code/devops_metrics.csv')
print(f"✅ Dataset loaded: {len(df)} samples, {len(df.columns)} features")

# Prepare features and target
X = df.drop('response_time_ms', axis=1)
y = df['response_time_ms']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"📈 Training set: {len(X_train)} samples")
print(f"📉 Test set: {len(X_test)} samples")
print()

# SOLUTION for TODO 2: Start an MLflow run
with mlflow.start_run():
    print("🔬 Training Linear Regression model...")

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print("📊 Model Performance:")
    print(f"   RMSE: {rmse:.2f}")
    print(f"   R² Score: {r2:.4f}")
    print(f"   MAE: {mae:.2f}")
    print()

    # SOLUTION for TODO 3: Log the model type parameter
    mlflow.log_param("model_type", "LinearRegression")

    # Log additional parameter
    mlflow.log_param("random_state", 42)

    # SOLUTION for TODO 4: Log the RMSE metric
    mlflow.log_metric("rmse", rmse)

    # Log additional metrics
    mlflow.log_metric("r2_score", r2)
    mlflow.log_metric("mae", mae)

    print("✅ Experiment tracked in MLflow!")
    print()
    print("🌐 Next Steps:")
    print("   1. Open MLflow UI (View Port → 5000)")
    print("   2. Click on 'DevOps-Response-Time-Prediction' experiment")
    print("   3. See your first tracked run with parameters and metrics!")

# Create success marker
os.makedirs('/root/markers', exist_ok=True)
with open('/root/markers/task1_baseline_complete.txt', 'w') as f:
    f.write("SUCCESS")

print()
print("=" * 60)
print("✅ Task 1 Complete: Baseline Experiment Tracked!")
print("=" * 60)
