# random.random() * 50 devuelve un número flotante aleatorio entre 0.00 y 50.99

import random

def aleatorio():
    for i in range(10):
        num = random.random()*50
        print(num)
    return num


print(aleatorio()) 	