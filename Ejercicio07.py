# random.random() * 25 + 10 devuelve un número flotante aleatorio entre 10.00 y 35.99

import random

def aleatorio():
    for i in range(10):
        num = random.random()*25+10
        print(num)
    return num


print(aleatorio()) 	