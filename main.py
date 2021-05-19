from flask import Flask, jsonify, request
from buscador import listaRevistas
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,resources={r"/filtroParametros/*": {"origins": "*"}})


filtro = [
   {
       "Categoria": "Revista 1",
       "Cuartil": "Q1",
       "Cantidad": 100
   } 
]

#Ruta que captura los parametros de busqueda de la forma 
#(http://localhost:5000/filtroParametros?area=Computer%20Science&categoria1=Q1&minArt=100&maxArt=1500&estado=premium)

@app.route('/filtroParametros', methods =["GET"])
def jsonRevistas():
    # Si no se encuentra la etiqueta, devuelve None
    area = request.args.get('area')
    categorias= []
    if request.args.get('categoria1') != '':
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria2') != '':
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria3') != '':
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria4') != '':
        categorias.append(True)
    else:
        categorias.append(False)

    minArt = request.args.get('minArt')
    maxArt = request.args.get('maxArt')
    
    estado = request.args.get('estado')

    return listaRevistas(area,categorias,minArt,maxArt,estado),200

#ruta que captura petición y devuelve una lista (local)
@app.route('/filtro', methods =["GET"])
def getFiltro():
    return jsonify(filtro), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)