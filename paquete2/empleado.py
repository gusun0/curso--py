class Empleado:
    def __init__(self,ocupacion,salario,vacaciones):
        self.__ocupacion = ocupacion 
        self.__salario = salario 
        self.__vacaciones = vacaciones

    def datosEmpleado(self):
        print(self.__ocupacion)
        print("Tiene un salario de:" ,self.__salario)
        print("Y sus días de vacaciones son:" ,self.__vacaciones)


