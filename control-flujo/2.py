#(2) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('ingresa palabra: \n')
i = 1
for i in range (10):
    print(i+1,palabra)
