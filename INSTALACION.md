# 📦 Guía de Instalación - MLOps Lab

## 🚀 Instalación Automática (Recomendada)

### Windows
```cmd
setup.bat
```

### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

## 🔧 Instalación Manual

### 1. Crear entorno virtual
```bash
# Windows
python -m venv mlops_env
mlops_env\Scripts\activate

# Linux/Mac
python -m venv mlops_env
source mlops_env/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Verificar instalación
```bash
python verify_environment.py
```

## 📋 Dependencias Requeridas

- **MLflow** ≥2.9.0 - Seguimiento de experimentos
- **scikit-learn** ≥1.3.0 - Algoritmos de ML
- **pandas** ≥2.0.0 - Manipulación de datos
- **numpy** ≥1.24.0 - Computación numérica
- **matplotlib** ≥3.7.0 - Visualización

## 🛠️ Instalación Personalizada

Si prefieres instalar manualmente:

```bash
python install_dependencies.py
```

## ✅ Verificación

Ejecuta el verificador de entorno:
```bash
python verify_environment.py
```

Deberías ver:
- ✅ Todos los paquetes instalados
- ✅ MLflow UI accesible en puerto 5000
- ✅ Dataset cargado correctamente

## 🆘 Solución de Problemas

### Error: MLflow UI no accesible
```bash
mlflow ui --host 0.0.0.0 --port 5000
```

### Error: Permisos en Linux/Mac
```bash
sudo pip install -r requirements.txt
```

### Error: Python no encontrado
Asegúrate de tener Python 3.8+ instalado:
```bash
python --version
```