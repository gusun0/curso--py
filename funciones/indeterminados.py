#def infinito(*args):
#    for arg in args:
#        print(arg)
#    
#infinito('assadsadasajkdh',True)

def infinito(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"--->",kwargs[kwarg])

infinito('a': 'hola', = 20, c = [1,2,3])
