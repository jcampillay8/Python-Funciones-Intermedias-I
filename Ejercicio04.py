import random
def randInt(min= ''  , max=''   ):
    num = random.randint(50,500)
    return num

print(randInt(min=50, max=500))
# debería imprimir un número aleatorio entre 50 y 500
