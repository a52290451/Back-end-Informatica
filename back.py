# Import Module
import json

# diccionario de categoria
def diccionarioCat = {"All subject areas": 0, "Agricultural and Biological Sciences": 1100, "Arts and Humanities": 1200, 
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

# metodo para listar revistas
def litaRevistas(area,categorias,minArt,maxArt):
    listaTotal = []

    return listaTotal

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