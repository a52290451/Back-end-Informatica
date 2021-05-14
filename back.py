# Import Module
import json

def filtradoParametros(area,categorias,minArt,maxArt):
    print("llegaste")

    # Create Dictionary
    value = {
        "area": area,
        "categoria1": categorias[0],
        "categoria2": categorias[1],
        "categoria3": categorias[2],
        "categoria4": categorias[3],
        "minArt": minArt,
        "maxArt": maxArt
    }
  
    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)