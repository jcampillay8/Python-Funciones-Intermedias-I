# round(num) devuelve el valor entero redondeado de num
import random

def aleatorio():
    for i in range(10):
        num = random.random()*10
        print(round(num))
    return round(num)


print(aleatorio()) 	