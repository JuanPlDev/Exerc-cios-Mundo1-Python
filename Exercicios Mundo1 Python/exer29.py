v = int(input("Qual a valocidade do carro: "))
m = (v - 80) * 7
if v > 80:
    print("Você ultrapassou a velocidade permitida, e foi multado com uma multa no valor de R${:.2f}".format(m))
else:
    print("Parabéns você está dentro da velocidade permitida ")