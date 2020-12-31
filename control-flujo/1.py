#(1)Escribir un programa que almacene la cadena de caracteres 
#contraseña en una variable, pregunte al usuario por la contraseña hasta queintroduzca la contraseña correcta.

con = 'contraseña'

dato = input('ingresa password: ')

while dato != con:
    print('contraseña incorrecta: \n')
    dato = input('ingresa password nuevamente: ')
else:
    print('contraseña correcta')

    




