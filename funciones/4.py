#(4) Crea una funcion que nos devuelva numeros pares.

def generaPares(limite):
    num = 1
    miLista = []

    while num <= limite:
        miLista.append(num*2)
        num += 1

    return miLista

print(generaPares(10))
