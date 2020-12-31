#3: Con operadores logicos, determina si una cadena de texto ingresada por el usuario
#tiene una longitud mayor o igual a 3 y a su vez es menor a 10. (tru o false)

cadena = input('ingresa una cadena:\n')
if len(cadena) >= 3 and len(cadena) < 10:
    print(True)
else:
    print(False)
