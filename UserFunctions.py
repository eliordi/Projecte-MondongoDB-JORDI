from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://jorcamacama:vCeDdv6PPz4yBwIE@jordflix.zdeahqa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["sample_mflix"]

def mostrarInfoPeli():

    print("\nMOSTRAR INFO D'UNA PEL·LÍCULA")

    title = input("\nIntrodueix el títol de la pel·lícula: ")

    pelicula = db.movies.find_one({'title': title})

    if pelicula:
        print(f"\nTítol: {pelicula['title']}")
        print(f"Any: {pelicula['year']}")
        print(f"Directors: {', '.join(pelicula['directors'])}")
        print(f"Argument: {pelicula['plot']}")
        print(f"Duració: {pelicula['runtime']} minuts")
        print(f"Gèners: {', '.join(pelicula['genres'])}")
    else:
        print(f"No s'ha trobat la pel·lícula '{title}'.")
    

def consultarPelisGenere():

    #Genres : Drama, Romance, Comdedy, Short, Western, Adventure, Fantasy, Family, War, Musical, Thriller, Animation, Music, Crime, Biography, History
    #Debe comprobar si el genero existe
    #Mostrar el title de las primeras 10 peliculas
    pass

def consultarActorsPeli():
    #Mostrar los actores (cast) de una película
    #Debemos comprobar si la pelicula existe
    
    print("\nMOSTRAR ACTORS D'UNA PEL·LÍCULA")

    title = input("\nIntrodueix el títol de la pel·lícula: ")

    pelicula = db.movies.find_one({'title': title})

    if pelicula:
        pass
    else:
        print(f"No s'ha trobat la pel·lícula '{title}'.")


def consultarCommentsPeli():
    #Mostrar los commentarios (collection comments) de una pelicula
    #Debemos pedir el title de la pelicula y si existe comprobar si tiene comentarios
    #En comments hay un documento movie_id que contiene el _id de la pelicula
    #De la collection comments sobre los comments de una pelicula solo quiero mostrar los campos name, text y date 
    
    print("\nMOSTRAR COMENTARIS D'UNA PEL·LÍCULA")

    title = input("\nIntrodueix el títol de la pel·lícula: ")

    pelicula = db.movies.find_one({'title': title})

    if pelicula:
        pass
    else:
        print(f"No s'ha trobat la pel·lícula '{title}'.")
    

def crearUsuari(usuari):
    #Crear un usuario de la collection users
    # name = usuari, email = pedir email, password = pedir password
    
    # Incluir opcion de crear un comentario en una pelicula, editar mis comentarios y borrarlos
    
    pass






