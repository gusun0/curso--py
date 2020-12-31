#Capacidad de tomar más de una forma

class Persona:
    def __init__(self):
        self.cedula = 12345

    def mensaje(self):
        print("Este msj viene de la clase Persona")

class Obrero(Persona):
    def __init__(self):
        self.especialista = 1
    def mensaje(self):
        print("Este msj viene de la clase obrero")

obrero_planta = Persona()
obrero_planta.mensaje()
