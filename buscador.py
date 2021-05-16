# Import Module
import json
import csv
from os.path import join, dirname, realpath

# diccionario de categoria
diccionarioCat = {"All subject areas": 0, "Agricultural and Biological Sciences": 1100, "Arts and Humanities": 1200, 
                                "Biochemistry, Genetics and Molecular Biology": 1300, "Business, Management and Accounting": 1400, 
                                "Chemical Engineering": 1500, 
                                "Chemistry": 1600, "Computer Science": 1700, "Decision Sciences": 1800, 
                                "Dentistry": 3500, "Earth and Planetary Sciences": 1900, "Economics, Econometrics and Finance": 2000, 
                                "Energy": 2100, "Engineering": 2200, "Environmental Science": 2300, 
                                "Health Professions": 3600, "Immunology and Microbiology": 2400, "Materials Science": 2500, 
                                "Mathematics": 2600, "Medicine": 2700, "Multidisciplinary": 1000, 
                                "Neuroscience": 2800, "Nursing": 2900, "Pharmacology, Toxicology and Pharmaceutics": 3000, 
                                "Physics and Astronomy": 3100, "Psychology": 3200, "Social Sciences": 3300, 
                                "Veterinary": 3400}

# metodo para listar revistas PRINCIPAL
def listaRevistas(area,categorias,minArt,maxArt,estado):
    listaTotal = []

    for i in range(0, 4):
        if categorias[i]:            
            archivoEntrada = nombreArchivo(area, i + 1) #se pasa area y categoria real. se obtiene el nombre del archivo
            listaArchivo = listaAreaCategoria(archivoEntrada, minArt, maxArt) #lista con las revistas
            listaTotal += listaArchivo #concatenado de listas 
    
    listaTotal = sorted(listaTotal, key=lambda rev:int(rev['Cantidad-articulos-ultimo']), reverse = True)
    
    if estado == 'free':
        return json.dumps(listaTotal[:3])
    elif estado == 'premium':
        return json.dumps(listaTotal)

# metodo de retorno del nombre del archivo csv a cargar
def nombreArchivo(area, categoria):
    if diccionarioCat[area] == 0:
        nombre = 'or' + 'q' + str(categoria) + 'Completo.csv'
        return nombre
    nombre = 'or' + str(diccionarioCat[area]) + 'q' + str(categoria) + 'Completo.csv'
    return nombre

# metodo que retorna la lista de revistas que están en el rango [min, max] de cantidad
def listaAreaCategoria(archivoEntrada, minimo, maximo):
    PATH = join(dirname(realpath(__file__)), 'repos/'+archivoEntrada)
    with open (PATH, 'r', encoding = 'UTF8') as archivo:
        lectorCSV = csv.DictReader(archivo)
        lista = []
        for revista in lectorCSV:
            cant = int(revista['Cantidad-articulos-ultimo'])
            if (cant >= int(minimo)) and (int(maximo) >= cant):
                lista.append(revista)
                
    return lista