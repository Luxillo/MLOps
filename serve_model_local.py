#!/usr/bin/env python3
"""
Servidor Local del Modelo - Desde directorio raíz

Sirve el modelo directamente usando Flask
"""

import mlflow.pyfunc
from flask import Flask, request, jsonify
import pandas as pd
import json

def main():
    # Cargar modelo
    print("🔄 Cargando modelo...")
    try:
        model = mlflow.pyfunc.load_model("models:/DevOps-Response-Predictor@staging")
        print("✅ Modelo cargado")
    except Exception as e:
        print(f"❌ Error cargando modelo: {e}")
        print("💡 Asegúrate de completar la Tarea 4 primero")
        return

    # Crear app Flask
    app = Flask(__name__)

    @app.route('/invocations', methods=['POST'])
    def predict():
        """Endpoint de predicción"""
        try:
            # Obtener datos JSON
            data = request.get_json()
            
            # Convertir a DataFrame
            if 'dataframe_split' in data:
                df = pd.DataFrame(
                    data['dataframe_split']['data'],
                    columns=data['dataframe_split']['columns']
                )
            else:
                return jsonify({"error": "Formato de datos inválido"}), 400
            
            # Hacer predicción
            predictions = model.predict(df)
            
            # Retornar resultado
            return jsonify({"predictions": predictions.tolist()})
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/health', methods=['GET'])
    def health():
        """Health check"""
        return jsonify({"status": "ok"})

    print("🚀 Iniciando servidor del modelo...")
    print("📡 API disponible en: http://localhost:8081/invocations")
    print("⏹️  Presiona Ctrl+C para detener")
    
    app.run(host='0.0.0.0', port=8081, debug=False)

if __name__ == "__main__":
    main()