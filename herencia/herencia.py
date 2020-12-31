class Persona:
    def __init__(self,nombre,edad,apellido,sexo):
        self.nombre = nombre 
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es:",self.nombre)
        print("La edad de la persona es:",self.edad)
        print("El apellido de la persona es:",self.apellido)
        print("El sexo de la persona es:",self.sexo)


miPersona = Persona("Pepe",25,"Gonzalez","M")
miPersona.datosPersonales()
print("\n\n")

class Empleado(Persona):
    def datosEmpleado(self,vacaciones,salario):
        print('Sus días de vacaciones son:',vacaciones)
        print('Su salario es:',salario)


miPersona2 = Empleado("Maria",22,"Gomez","F")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(30,2000)


