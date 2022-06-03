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

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

#Ruta que captura los parametros de busqueda de la forma 
#(http://localhost:5000/filtroParametros?area=Computer%20Science&categoria1=Q1&minArt=100&maxArt=1500&estado=Premium)

@app.route('/filtroParametros', methods =["GET"])
def jsonRevistas():
    # Si no se encuentra la etiqueta, devuelve None
    area = request.args.get('area')
    categorias = []
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

    jsonx = listaRevistas(area,categorias,minArt,maxArt,estado)

    return jsonx,200

#ruta que captura peticion y devuelve una lista (local)
@app.route('/filtro', methods =["GET"])
def getFiltro():
    return jsonify(filtro), 200




#------------------ Metodos de prueba --------------------

users = [
   {
       "Username": "Admin",
       "Age": "25"

   },
   {
       "Username": "user 1",
       "Age": "18"

   } 
]

#ruta que captura peticion, filtra por nombre de usuario y retorna la informacion de ese usuario
@app.route('/users/<string:username>', methods =["GET"])
def getUsersByUsername(username):
    result = next((user for user in users if user["Username"] == username),None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404

#ruta que captura peticion, filtra por nombre de usuario y retorna la informacion de ese usuario
@app.route('/filtro/<string:categoria>/<string:cuartil>/<int:cantidad>', methods =["GET"])
def getRevistasByCategoria(categoria):
    result = next((comp for comp in filtro if comp["Categoria"] == categoria),None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404
def getRevistasByCuartil(cuartil):
    result = next((comp for comp in filtro if comp["Cuartil"] == cuartil),None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404

#ruta que captura peticion y devuelve una lista de usuarios
@app.route('/users', methods =["GET"])
def getAllUsers():
    return jsonify(users), 200

#Crear usuarios
@app.route('/users', methods =["POST"])
def addUser():
    body = json.loads(request.data)
    
    userName = body["Username"]
    age = body["Age"]
    
    newUser = {
        "Username": userName,
        "Age": age
    }
    
    users.append(newUser)
    return jsonify(newUser), 200

#Borrar usuarios

@app.route('/users/<string:username>', methods=["DELETE"])
def deleteUser(username):
    userFound = None
    for index, user in enumerate(users):
        if user["Username"] == username:
            userFound = user
            users.pop(index)
    if userFound is not None:
        return "User deleted", 200
    else:
        return "User not found", 404





if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True,host='0.0.0.0',port=80)