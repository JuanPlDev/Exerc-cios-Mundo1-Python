from math import sqrt
co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
x = (co * co + ca * ca)
print("A hipotenusa do triângulo vai medir {:.2}".format(sqrt(x)))
