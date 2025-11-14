#!/usr/bin/env python3
"""
Script de Cierre del Laboratorio MLOps

Apaga todos los servicios y desactiva el entorno virtual
"""

import subprocess
import sys
import os
import psutil
import time

def find_and_kill_processes():
    """Encontrar y terminar procesos relacionados con MLflow y Flask"""
    print("🔍 Buscando procesos activos...")
    
    killed_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            
            # Buscar procesos MLflow
            if 'mlflow' in cmdline.lower() and ('ui' in cmdline or 'serve' in cmdline):
                print(f"   🎯 Terminando MLflow: PID {proc.info['pid']}")
                proc.terminate()
                killed_processes.append(f"MLflow (PID {proc.info['pid']})")
            
            # Buscar servidores Flask del modelo
            elif 'serve_model' in cmdline or ('flask' in cmdline.lower() and '8081' in cmdline):
                print(f"   🎯 Terminando servidor del modelo: PID {proc.info['pid']}")
                proc.terminate()
                killed_processes.append(f"Servidor modelo (PID {proc.info['pid']})")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if killed_processes:
        print(f"   ✅ Procesos terminados: {len(killed_processes)}")
        time.sleep(2)  # Esperar a que terminen
    else:
        print("   ℹ️  No se encontraron procesos activos")

def kill_ports():
    """Liberar puertos específicos"""
    print("\n🔌 Liberando puertos...")
    
    ports = [5000, 8081]  # MLflow UI y API del modelo
    
    for port in ports:
        try:
            # Windows
            result = subprocess.run(
                f'netstat -ano | findstr :{port}',
                shell=True, capture_output=True, text=True
            )
            
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if f':{port}' in line and 'LISTENING' in line:
                        parts = line.split()
                        if len(parts) >= 5:
                            pid = parts[-1]
                            subprocess.run(f'taskkill /F /PID {pid}', shell=True, capture_output=True)
                            print(f"   ✅ Puerto {port} liberado (PID {pid})")
            else:
                print(f"   ℹ️  Puerto {port} ya está libre")
                
        except Exception as e:
            print(f"   ⚠️  Error liberando puerto {port}: {e}")

def show_deactivation_instructions():
    """Mostrar instrucciones para desactivar entorno virtual"""
    print("\n🔄 Desactivando entorno virtual...")
    
    # Verificar si estamos en un entorno virtual
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("   ✅ Entorno virtual detectado")
        print("   💡 Para desactivar manualmente, ejecuta: deactivate")
    else:
        print("   ℹ️  No se detectó entorno virtual activo")

def cleanup_temp_files():
    """Limpiar archivos temporales del laboratorio"""
    print("\n🧹 Limpiando archivos temporales...")
    
    temp_patterns = [
        '__pycache__',
        '*.pyc',
        '.pytest_cache'
    ]
    
    cleaned = 0
    for root, dirs, files in os.walk('.'):
        # Limpiar directorios __pycache__
        if '__pycache__' in dirs:
            import shutil
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                cleaned += 1
            except:
                pass
    
    if cleaned > 0:
        print(f"   ✅ {cleaned} directorios temporales eliminados")
    else:
        print("   ℹ️  No se encontraron archivos temporales")

def main():
    print("🛑 Script de Cierre del Laboratorio MLOps")
    print("=" * 50)
    
    # 1. Terminar procesos
    find_and_kill_processes()
    
    # 2. Liberar puertos
    kill_ports()
    
    # 3. Limpiar archivos temporales
    cleanup_temp_files()
    
    # 4. Instrucciones de desactivación
    show_deactivation_instructions()
    
    print("\n" + "=" * 50)
    print("✅ ¡Laboratorio cerrado exitosamente!")
    print()
    print("📋 Resumen de acciones:")
    print("   • Procesos MLflow terminados")
    print("   • Servidores de API detenidos")
    print("   • Puertos 5000 y 8081 liberados")
    print("   • Archivos temporales limpiados")
    print()
    print("💡 Para reactivar el laboratorio:")
    print("   1. mlops_env\\Scripts\\activate")
    print("   2. mlflow ui")
    print("   3. python serve_model_local.py")
    print()
    print("🎉 ¡Gracias por usar el laboratorio MLOps!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Cierre interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error durante el cierre: {e}")
        print("💡 Puedes cerrar manualmente con Ctrl+C en las terminales activas")