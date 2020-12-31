def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

op1 = int(input('introduce el valor 1: '))
op2 = int(input('introduce el valor 2: '))

operacion = input('introduce la operacíón a realizar\n(suma, resta, multiplicación, división\n')

if(operacion == 'suma'):
    print(suma(op1,op2))
elif(operacion == 'resta'):
    print(resta(op1,op2))
elif(operacion == 'multiplicar'):
    print(multiplicacion(op1,op2))
elif(operacion == 'dividir'):
    try:
        print(division(op1,op2))
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
else:
    print('error')

print('ejecutando')




