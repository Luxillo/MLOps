# 📚 Documentación de Tareas MLOps

## 🎯 Resumen General

Este proyecto contiene 4 tareas progresivas para aprender MLflow:

1. **Tarea 1**: Experimento base con Regresión Lineal
2. **Tarea 2**: Ajuste de hiperparámetros con Random Forest
3. **Tarea 3**: Comparación de múltiples modelos
4. **Tarea 4**: Registro y versionado de modelos

---

## 📊 Tarea 1: Experimento Base (`task_1_baseline_experiment.py`)

### 🎯 Objetivo
Crear tu primer experimento MLflow con un modelo simple de Regresión Lineal.

### 🔧 Funcionalidad
- Carga dataset de métricas DevOps (5 características → tiempo de respuesta)
- Entrena modelo LinearRegression
- Calcula métricas: RMSE, R², MAE
- Registra parámetros y métricas en MLflow

### 📝 TODOs a Completar
1. **Línea 26**: `mlflow.set_experiment("DevOps-Response-Time-Prediction")`
2. **Línea 49**: `with mlflow.start_run():`
3. **Línea 73**: `mlflow.log_param("model_type", "LinearRegression")`
4. **Línea 81**: `mlflow.log_metric("rmse", rmse)`

### 🎓 Conceptos Aprendidos
- Configurar experimento MLflow
- Iniciar ejecución de seguimiento
- Registrar parámetros del modelo
- Registrar métricas de rendimiento

### 📈 Resultados Esperados
- R² ≈ 0.85-0.90
- RMSE ≈ 15-25 ms
- Experimento visible en MLflow UI

---

## 🔬 Tarea 2: Ajuste de Hiperparámetros (`task_2_hyperparameter_tuning.py`)

### 🎯 Objetivo
Comparar diferentes configuraciones de Random Forest para encontrar la óptima.

### 🔧 Funcionalidad
- Prueba 3 valores de `max_depth`: [5, 10, 15]
- Entrena RandomForestRegressor para cada configuración
- Registra hiperparámetros y métricas de cada ejecución
- Usa etiquetas para organizar experimentos

### 📝 TODOs a Completar
1. **Línea 49**: `mlflow.log_param("max_depth", depth)`
2. **Línea 71**: `mlflow.log_params({"n_estimators": 100, "random_state": 42})`
3. **Línea 78**: `mlflow.log_metric("r2_score", r2)`
4. **Línea 87**: `mlflow.set_tag("model_family", "RandomForest")`

### 🎓 Conceptos Aprendidos
- Registro individual de parámetros
- Registro en lote de múltiples parámetros
- Comparación sistemática de configuraciones
- Uso de etiquetas para organización

### 📈 Resultados Esperados
- max_depth=15 generalmente da mejor R²
- R² ≈ 0.90-0.95
- 3 ejecuciones comparables en MLflow UI

---

## 🏆 Tarea 3: Comparación de Modelos (`task_3_model_comparison.py`)

### 🎯 Objetivo
Entrenar y comparar 3 algoritmos diferentes para seleccionar el mejor.

### 🔧 Funcionalidad
- **LinearRegression**: Rápido, simple, baseline
- **RandomForest**: Potente, ensemble, robusto
- **GradientBoosting**: Lento, muy preciso, estado del arte
- Guarda modelos como artefactos MLflow

### 📝 TODOs a Completar
1. **Línea 54**: `mlflow.log_param("model_name", model_name)`
2. **Línea 70**: `mlflow.log_metrics({"rmse": rmse, "r2_score": r2, "mae": mae})`
3. **Línea 79**: `mlflow.sklearn.log_model(model, "model")`

### 🎓 Conceptos Aprendidos
- Comparación de arquitecturas de modelos
- Registro eficiente de múltiples métricas
- Guardado de modelos como artefactos
- Selección del mejor modelo basado en métricas

### 📈 Resultados Esperados
- **LinearRegression**: R² ≈ 0.85
- **RandomForest**: R² ≈ 0.92
- **GradientBoosting**: R² ≈ 0.94 (ganador típico)

---

## 🚀 Tarea 4: Registro de Modelos (`task_4_model_registry.py`)

### 🎯 Objetivo
Registrar el mejor modelo en MLflow Registry para despliegue en producción.

### 🔧 Funcionalidad
- Entrena GradientBoostingRegressor (mejor de Tarea 3)
- Registra modelo en MLflow Model Registry
- Asigna alias "staging" para control de versiones
- Carga modelo registrado para hacer predicciones

### 📝 TODOs a Completar
1. **Línea 67**: `mlflow.sklearn.log_model(model, "model")`
2. **Línea 81**: `mlflow.register_model(model_uri, "DevOps-Response-Predictor")`
3. **Línea 94**: `client.set_registered_model_alias(model_name, "staging", model_version)`
4. **Línea 110**: `mlflow.pyfunc.load_model(model_uri_registry)`

### 🎓 Conceptos Aprendidos
- Registro de modelos para producción
- Control de versiones de modelos
- Uso de aliases (staging, production)
- Carga de modelos desde registry

### 📈 Resultados Esperados
- Modelo registrado como "DevOps-Response-Predictor v1"
- Alias "staging" asignado
- Modelo cargable para predicciones
- Visible en pestaña "Models" de MLflow UI

---

## 🔄 Flujo de Trabajo Completo

```
Tarea 1: Baseline → Tarea 2: Tuning → Tarea 3: Comparación → Tarea 4: Registro
    ↓                    ↓                    ↓                      ↓
Aprende MLflow      Optimiza modelo     Selecciona mejor      Despliega producción
```

## 📊 Métricas Clave

- **RMSE**: Error cuadrático medio (menor = mejor)
- **R²**: Coeficiente de determinación (mayor = mejor, máx = 1.0)
- **MAE**: Error absoluto medio (menor = mejor)

## 🎯 Criterios de Éxito

✅ Todos los TODOs completados
✅ Experimentos visibles en MLflow UI
✅ Métricas registradas correctamente
✅ Modelo registrado en Model Registry
✅ Comprensión del flujo MLOps completo