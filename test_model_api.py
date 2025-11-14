#!/usr/bin/env python3
"""
Prueba Simple del Modelo API

Prueba el modelo servido localmente
"""

import requests
import json
import time

def test_model():
    """Probar el modelo con datos de muestra"""
    print("🧪 Probando API del modelo...")
    
    # Verificar que el servidor esté disponible
    try:
        health_response = requests.get("http://localhost:8081/health", timeout=5)
        if health_response.status_code != 200:
            print("❌ Servidor no disponible")
            return
    except:
        print("❌ No se puede conectar al servidor")
        print("💡 Ejecuta primero: python serve_model_local.py")
        return
    
    # Datos de prueba
    test_data = {
        "dataframe_split": {
            "columns": ["cpu_usage", "memory_usage", "disk_io_mbps", "network_latency_ms", "concurrent_users"],
            "data": [
                [75.5, 68.2, 45.3, 12.1, 150],  # Carga alta
                [25.0, 30.5, 15.2, 5.8, 50],    # Carga baja
                [90.2, 85.7, 78.4, 25.3, 300]   # Carga crítica
            ]
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:8081/invocations",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data),
            timeout=30
        )
        
        if response.status_code == 200:
            predictions = response.json()["predictions"]
            
            print("✅ ¡API funcionando!")
            print("\n📈 Predicciones:")
            scenarios = ["Carga Alta", "Carga Baja", "Carga Crítica"]
            
            for scenario, pred in zip(scenarios, predictions):
                print(f"   {scenario}: {pred:.2f} ms")
                
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Respuesta: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_model()