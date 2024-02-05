from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://jorcamacama:<password>@jordflix.zdeahqa.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


def mostrarInfoPeli():
    pass

def consultarPelisGenere():
    pass

def consultarActorsPeli():
    pass

def consultarCommentsPeli():
    pass

def crearUsuari():
    
    # Incluir opcio de crear un comentari, editarlo i borrarlo
    
    pass






