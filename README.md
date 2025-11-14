# Lab 1: Fundamentos de MLOps - Seguimiento de Experimentos con MLflow

## 🎯 Lo que Aprenderás

Domina MLflow a través de 4 tareas prácticas progresivas:

1. **Tarea 1**: Seguimiento de experimento base (4 TODOs)
2. **Tarea 2**: Ajuste de hiperparámetros (4 TODOs)
3. **Tarea 3**: Comparación de múltiples modelos (3 TODOs)
4. **Tarea 4**: Registro y versionado de modelos (4 TODOs)

**Total**: 15 TODOs para completar en ~50 minutos

---

## 🌐 Accediendo a la UI de MLflow

**Después de ejecutar `mlflow ui`**, para acceder:

1. **Haz clic en el menú hamburguesa (≡)** en la esquina superior derecha
2. **Selecciona "View Port"**
3. **Ingresa el puerto**: `5000`
4. **Haz clic en "Open Port"**
5. **La UI de MLflow se abre** en una nueva pestaña del navegador

💡 **Mantén esta pestaña abierta** - ¡la usarás después de cada tarea!

---

## 📊 El Dataset: devops_metrics.csv

Predecirás el **tiempo de respuesta de la API** a partir de métricas del sistema:

**Características** (lo que monitoreas):
- Uso de CPU (%)
- Uso de memoria (%)
- E/S de disco (MB/s)
- Latencia de red (ms)
- Usuarios concurrentes (cantidad)

**Objetivo** (lo que predices):
- Tiempo de respuesta (milisegundos)

**Uso en el Mundo Real**:
- Planificación de capacidad
- Decisiones de autoescalado
- Monitoreo de SLA
- Optimización de rendimiento

---

## 🔧 Configuración del Entorno

Todo está preconfigurado:

- ✅ MLflow (última versión estable)
- ✅ UI de MLflow ejecutándose en puerto 5000
- ✅ Directorio de seguimiento: `/root/mlruns`
- ✅ Dataset: `/root/code/devops_metrics.csv`
- ✅ Paquetes de Python: scikit-learn, pandas, numpy, matplotlib

---

## 🚀 Iniciar el Laboratorio

### 1. Activar entorno virtual
```bash
# Windows
mlops_env\Scripts\activate

# Linux/Mac
source mlops_env/bin/activate
```

### 2. Iniciar MLflow UI
```bash
# Opción 1: Comando estándar
mlflow ui

# Opción 2: Comando completo (si hay problemas)
mlflow ui --host 0.0.0.0 --port 5000
```

### 3. Verificar acceso
- ✅ Terminal muestra: `Listening at: http://127.0.0.1:5000`
- ✅ UI accesible en puerto 5000 (ver instrucciones arriba)

💡 **Mantén la terminal abierta** - MLflow UI debe ejecutarse durante todo el lab

---

## 🚀 Conceptos Clave

### ¿Qué es MLflow?

MLflow resuelve el **"problema del caos de ML"**:

**Sin MLflow**:
- ❌ ¿Qué hiperparámetros dieron 95% de precisión?
- ❌ ¿Podemos reproducir el modelo del mes pasado?
- ❌ ¿Qué cambió entre v1 y v2?
- ❌ ¿Cómo revertimos un modelo malo?

**Con MLflow**:
- ✅ Cada experimento registrado automáticamente
- ✅ Seguimiento de parámetros y métricas
- ✅ Versionado de modelos (como Git)
- ✅ Reversión con un clic
- ✅ Colaboración en equipo

### Los Tres Componentes de MLflow

1. **Tracking**: Registrar experimentos (parámetros, métricas, código)
2. **Model Registry**: Control de versiones para modelos
3. **Projects**: Flujos de trabajo de ML reproducibles

Este lab cubre Tracking (Tareas 1-3) y Registry (Tarea 4).

### Por qué Importa el Versionado de Modelos

Escenario de producción:
```
v1.0 (Producción) → 92% precisión ✅
v1.1 (Staging)    → 94% precisión 🎯 (¡despliega esto!)
v1.2 (Dev)        → 89% precisión ❌ (bug encontrado, no desplegar)
```

MLflow Registry te permite:
- Rastrear todas las versiones
- Etapas de modelos (Dev → Staging → Producción)
- Revertir instantáneamente si v1.1 falla

---

## 📝 Resumen de Tareas

### Tarea 1: Experimento Base (15 min)
**Objetivo**: Rastrear tu primer experimento de ML

**Aprenderás**:
- Establecer nombre del experimento
- Iniciar ejecución de MLflow
- Registrar parámetros (model_type, random_state)
- Registrar métricas (RMSE, R², MAE)

**Después de completar**: Abrir UI de MLflow → ¡Ver tu experimento!

---

### Tarea 2: Ajuste de Hiperparámetros (15 min)
**Objetivo**: Comparar RandomForest con diferentes configuraciones

**Aprenderás**:
- Registrar parámetros individuales (`log_param`)
- Registrar parámetros en lote (`log_params`)
- Registrar múltiples métricas
- Etiquetar experimentos para organización

**Después de completar**: UI de MLflow → Comparar ejecuciones → ¡Encontrar mejor configuración!

---

### Tarea 3: Comparación de Modelos (10 min)
**Objetivo**: Entrenar 3 modelos, elegir el mejor

**Modelos**:
- LinearRegression (rápido, simple)
- RandomForest (poderoso, ensemble)
- GradientBoosting (lento, preciso)

**Aprenderás**:
- Comparar arquitecturas de modelos
- Registrar múltiples métricas a la vez
- Guardar artefactos de modelos

**Después de completar**: UI de MLflow → Ordenar por R² → ¡Ver ganador!

---

### Tarea 4: Registro de Modelos (10 min)
**Objetivo**: Registrar el mejor modelo para producción

**Aprenderás**:
- Registrar modelo en MLflow Registry
- Asignar versiones de modelo
- Transicionar a etapa "Staging"
- Cargar modelo registrado para predicciones

**Después de completar**: UI de MLflow → Pestaña Models → ¡Ver modelo registrado!

---

## 🧪 Pruebas del Modelo (Bonus)

**Objetivo**: Probar tu modelo registrado como API REST

**Ubicación**: Directorio `test/`

**Métodos disponibles**:
1. **Automático**: `python test/test_model_deployment.py`
2. **Manual**: `python test/serve_model.py` + `python test/test_requests.py`
3. **Curl**: `mlflow models serve` + comandos curl

**Aprenderás**:
- Servir modelos MLflow como API
- Enviar requests HTTP al modelo
- Probar diferentes escenarios de carga
- Validar predicciones en tiempo real

**Después de completar**: ¡Modelo listo para producción!

### 🚀 Prueba Rápida del Modelo

```bash
# Terminal 1: Servir modelo
python serve_model_local.py

# Terminal 2: Probar modelo
python test_model_api.py
```

---

## 💡 Consejos Pro

1. **Usa `Ctrl+G` / `Cmd+G`** para saltar a números de línea
2. **Lee los comentarios TODO** - contienen pistas
3. **Revisa la UI de MLflow después de cada tarea** - visualiza tu progreso
4. **Compara ejecuciones** - usa la tabla de comparación de la UI
5. **Experimenta libremente** - ¡MLflow rastrea todo!

---

## 🎓 Aplicaciones del Mundo Real

Este lab enseña fundamentos para:

**Detección de Deriva de Modelos**:
- Rastrear rendimiento del modelo a lo largo del tiempo
- Alertar cuando la precisión cae bajo el umbral
- Comparar nuevo modelo vs línea base

**Pipelines de ML CI/CD**:
- Reentrenamiento automatizado con nuevos datos
- Versionado de modelos en pipeline de despliegue
- Reversión a versión anterior si hay problemas

**Colaboración en Equipo**:
- Historial de experimentos compartido
- Comparar modelos de compañeros de equipo
- Resultados reproducibles

**Despliegue en Producción**:
- Flujo de trabajo de promoción Staging → Producción
- Pruebas A/B de diferentes versiones de modelo
- Despliegues blue-green

---

## 🏢 Empresas que Usan MLflow

- **Netflix**: Experimentos de modelos de recomendación
- **Uber**: Versionado de modelos de precios y ETA
- **Databricks**: Creó MLflow, lo usa para todo ML
- **Microsoft**: Integración con Azure ML
- **AWS**: Seguimiento de MLflow en SageMaker

---

## ✅ Criterios de Éxito

Al final, podrás:

1. Rastrear experimentos de ML con parámetros y métricas
2. Comparar configuraciones de hiperparámetros
3. Seleccionar el mejor modelo de múltiples opciones
4. Registrar modelos con control de versiones
5. Navegar la UI de MLflow con confianza
6. Entender flujos de trabajo de ML en producción

**Tiempo Total**: ~50 minutos
**TODOs Totales**: 15 (todos claramente marcados)

¡Construyamos habilidades de ML listas para producción! 🚀
