
# importando toda a biblioteca
#import math
#num = int(input("Digite um número: "))
#raiz = math.sqrt(num)
#print("A raiz de {} é {}".format(num, math.ceil(raiz)))

#importa só a biblioteca especifica
from math import sqrt,ceil
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é {}".format(num, ceil(raiz)))