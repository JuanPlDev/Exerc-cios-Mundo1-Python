import math
angulo = float(input("Digite o valor de um angulo que deseja calcular: "))
seno = math.sin(math.radians(angulo))
print('O seno de {:.2f} graus é {:.2f} graus'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O cosseno de {:.2f} graus é {:.2f} graus".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("A tangante de {:.2f} graus é {:.2f} graus".format(angulo, tangente))

