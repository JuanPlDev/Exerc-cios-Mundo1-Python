import random
num = random.randint(0,5)
n = int(input("Digite um número para tentar advinhar oque eu pensei: "))
if n == num:
    print("O numero que eu pensei foi {}, Parabéns você venceu".format(num))
else:
    print("O número que eu pensei foi {}, Você perdeu ".format(num))