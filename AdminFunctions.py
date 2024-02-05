from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://jorcamacama:vCeDdv6PPz4yBwIE@jordflix.zdeahqa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["sample_mflix"]


def crearArray():    
    array = []
    print("Intro en blanc si vols eixir")
    while(True): 
        objecte = input("-> ")
        if objecte == "":
            break
        else: 
            array.append(objecte)

    return array

def crearPeli():

    print("\n CREAR UNA PEL·LÍCULA")
    
    title = input("Títol -> ")
    print("Directors: ")
    directors = crearArray()
    plot = input("Trama -> ")
    print("Gèneres: ")
    genres = crearArray()
    runtime = input("Duració -> ")
    print("Llenguatges: ")
    languages = crearArray()
    print("Actors principals: ")
    cast = crearArray()

    peli = {
        "title": title,
        "directors": directors,
        "plot": plot,
        "genres": genres,
        "runtime": runtime,
        "languages": languages,
        "cast": cast
    }

    db.movies.insert_one(peli)

    
def consultarCommentsUsuari():

    print("\n CONSULTAR COMENTARIS D'UN USUARI")

    collection = db.users

    users = collection.find()
    print("LLISTAT DE TOTS ELS USUARIS: ")
    for user in users:
        print("-> ", user["name"])

    user = input("\nIntrodueix el nom de l'usuari: ")

    commentsUsu = db.comments.find({'name': user}, {'name', 'movie_id', 'text'})
    print(f"\nAquests son tots els comentaris de l'usuari {user}")
    for comment in commentsUsu:
        print("\n-> ",comment)


def eliminarPeli():
    pass

def eliminarComments():
    pass

def eliminarUser():
    pass

