#(2) Solicitar al usuario que ingrese su dirección email. 
#Imprimir un mensaje indicando si la dirección es válida o no, 
#valiéndose de una función para decidirlo. 
#Una dirección se considerará válida si contiene el símbolo "@".

def validar(email):
    caracterBuscado = '@'
    #emailValido = False
    for i in email:
        if i == caracterBuscado:
            return True
    return False

direccion = input('direccion: ')
if(validar(direccion)):
    print('valido')
else:
    print('invalido')

