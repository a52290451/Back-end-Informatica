from flask import Flask, jsonify, request
from back import listaRevistas
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
#(http://localhost:5000/filtroParametros?area=Energy&categoria1=Q1&categoria2=Q2&minArt=10&maxArt=1000&estado=free)

@app.route('/filtroParametros', methods =["GET"])
def jsonRevistas():
    # Si no se encuentra la etiqueta, devuelve None
    area = request.args.get('area')
    categorias= []
    if request.args.get('categoria1') != None:
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria2') != None:
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria3') != None:
        categorias.append(True)
    else:
        categorias.append(False)
    if request.args.get('categoria4') != None:
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




#------------------ Métodos de prueba --------------------

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

#ruta que captura petición, filtra por nombre de usuario y retorna la información de ese usuario
@app.route('/users/<string:username>', methods =["GET"])
def getUsersByUsername(username):
    result = next((user for user in users if user["Username"] == username),None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404

#ruta que captura petición, filtra por nombre de usuario y retorna la información de ese usuario
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

#ruta que captura petición y devuelve una lista de usuarios
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
    app.run(debug=True)

