#!/usr/bin/env python3
"""
Instalador de Dependencias para MLOps Lab
Este script instala automáticamente todas las dependencias necesarias.
"""

import subprocess
import sys
import os

def install_package(package):
    """Instalar un paquete usando pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🚀 Instalador de Dependencias MLOps Lab")
    print("=" * 50)
    
    # Leer requirements.txt
    requirements_file = "requirements.txt"
    if not os.path.exists(requirements_file):
        print(f"❌ Archivo {requirements_file} no encontrado")
        return 1
    
    with open(requirements_file, 'r') as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    print(f"📦 Instalando {len(packages)} paquetes...")
    print()
    
    failed_packages = []
    
    for package in packages:
        print(f"⏳ Instalando {package}...")
        if install_package(package):
            print(f"✅ {package} instalado correctamente")
        else:
            print(f"❌ Error instalando {package}")
            failed_packages.append(package)
        print()
    
    print("=" * 50)
    
    if not failed_packages:
        print("✅ Todas las dependencias instaladas correctamente")
        print("🔍 Ejecuta 'python verify_environment.py' para verificar")
        return 0
    else:
        print(f"❌ {len(failed_packages)} paquetes fallaron:")
        for pkg in failed_packages:
            print(f"   - {pkg}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)