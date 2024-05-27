from flask import Flask, jsonify, request
import csv
import json
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Función para leer archivo CSV
def leer_csv(archivo):
    with open(archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

# Función para leer archivo JSON
def leer_json(archivo):
    with open(archivo) as jsonfile:
        data = json.load(jsonfile)
        return data

# Función para leer archivo XML
def leer_xml(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    data = []
    for usuario in root.findall('usuario'):
        data.append({
            "nombre": usuario.find('nombre').text,
            "edad": usuario.find('edad').text,
            "email": usuario.find('email').text
        })
    return data

# Ruta para la página de inicio
@app.route('/')
def index():
    return 'Hola, este es mi servidor Flask.'

@app.route('/datos', methods=['GET'])
def obtener_datos():
    formato = request.args.get('formato')
    if formato == 'csv':
        return jsonify(leer_csv('datos.csv'))  # Nombre del archivo CSV
    elif formato == 'json':
        return jsonify(leer_json('datos.json'))  # Nombre del archivo JSON
    elif formato == 'xml':
        return jsonify(leer_xml('datos.xml'))  # Nombre del archivo XML
    else:
        return jsonify({"mensaje": "Formato no válido"})

if __name__ == '__main__':
    app.run(debug=True)

