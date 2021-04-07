import random
def randInt(min='' , max=100   ):
    num = random.randint(min,max)
    return num

print(randInt(min=50))
# debería imprimir un número aleatorio entre 50 a 100

