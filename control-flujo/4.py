#(4)Escribir un programa que muestre el eco de todo lo que el usuario 
#introduzca hasta que el usuario escriba “salir” que terminará.

palabra = input('ingresa palabra: \n')

while palabra != 'salir':
    print('ingresa otra palabra')
    palabra = input('ingresa palabra: \n')
else:
    print('ingresaste salir')
    



