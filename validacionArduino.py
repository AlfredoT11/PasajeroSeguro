import serial, time
from manejoDB import buscarUsuario, nuevoRegistro

def verificarDatosEnviados():
    
    infoPuerto = serial.Serial('COM3', 9600)
    print("Iniciando...")
    time.sleep(3)
    print("Inicio exitoso")
 

    for i in range(10):
        identificador = infoPuerto.readline()
        #print("Identificador recibido: ", identificador)
        #print("Tipo: ", type(identificador))
        #print("String: ", identificador.decode("utf-8"))

        #usuarioNuevo = {
        #    "_id" : identificador.decode("utf-8")[0:len(identificador.decode("utf-8"))-2],
        #    "nombre" : "Alfredo",
        #    "segundoNombre" : "Tonatiuh",
        #    "paterno" : "Díaz",
        #    "materno" : "Gómez",
        #    "escuela" : "ESCOM"
        #}

        #nuevoRegistro(usuarioNuevo)

        buscarUsuario(identificador.decode("utf-8")[0:len(identificador.decode("utf-8"))-2])



verificarDatosEnviados()