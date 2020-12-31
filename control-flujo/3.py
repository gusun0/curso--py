#(3) Escribir un programa que pregunte al usuario su edad 
#y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input('edad: \n'))
for i in range(edad-1):
    print(str(i+1) +' años')

