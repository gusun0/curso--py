class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: " , self.nombre)
        print("La edad de la persona es: " ,(self.edad))
        print("El sexo de la persona es: ", self.sexo)


miPersona = Persona('Jorge',29,'M')
miPersona2 = Persona('Abraham',25,'M')
miPersona3 = Persona('Ana',19,'F')


miPersona.datosPersonales()
miPersona2.datosPersonales()
miPersona3.datosPersonales()
