import serial, time
from manejoDB import buscarUsuario

def verificarDatosEnviados():
    
    infoPuerto = serial.Serial('COM3', 9600)
    print("Iniciando...")
    time.sleep(3)
    print("Inicio exitoso")

    for i in range(2):
        identificador = infoPuerto.readline()
        print("Identificador recibido: ", identificador)
        print("Tipo: ", type(identificador))
        print("String: ", identificador.decode("utf-8"))
        buscarUsuario(identificador.decode("utf-8")[0:len(identificador.decode("utf-8"))-2])



verificarDatosEnviados()