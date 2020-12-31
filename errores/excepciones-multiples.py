try:
    c = int(input('ingresa un valor: '))
    c/0
except ValueError:
    print('error no se puede sumar una cadena texto')
except Exception as c:
    print(type(c).__name__)

