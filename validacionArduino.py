import serial, time

def verificarDatosEnviados():
    
    infoPuerto = serial.Serial('Puerto aquí', 9600)
    print("Iniciando...")
    time.sleep(3)
    print("Inicio exitoso")

    identificador = infoPuerto.readline()
    print("Identificador recibido: ", identificador)
