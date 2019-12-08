import pymongo

def nuevoRegistro(infoUsuario):

    uri = "mongodb://adiazg1404:Jx0UTPrHqPbDN8FwfrmCheZpOifEsRH0DzyYW5M4PilGkGzP8uQ8qT9xfSQQA9mjhwGIxhfF0ai0VEYAkvzmkQ==@adiazg1404.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    #client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["TransporteSeguro"]
    collectionUsuario = db["Usuario"]

    nuevoUsuario = collectionUsuario.insert_one(infoUsuario)
    print("ID nuevo: ", nuevoUsuario.inserted_id)

    buscarUsuario(nuevoUsuario.inserted_id)

def buscarUsuario(idUsuario):

    uri = "mongodb://adiazg1404:Jx0UTPrHqPbDN8FwfrmCheZpOifEsRH0DzyYW5M4PilGkGzP8uQ8qT9xfSQQA9mjhwGIxhfF0ai0VEYAkvzmkQ==@adiazg1404.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)

    #client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["TransporteSeguro"]
    collectionUsuario = db["Usuario"]

    usuario = collectionUsuario.find_one({"_id" : idUsuario})

    if(usuario == None):
        print("Usuario no encontrado")
        return -1
    else:
        print("Usuario", usuario)
        print("ID: ", usuario['_id'])


#usuarioNuevo = {
#    "_id" : "13720737217186",
#    "nombre" : "Alfredo",
#    "segundoNombre" : "Tonatiuh",
#    "paterno" : "Díaz",
#    "materno" : "Gómez",
#    "escuela" : "ESCOM"
#}

#nuevoRegistro(usuarioNuevo)