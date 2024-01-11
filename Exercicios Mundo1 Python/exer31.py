v = int(input("Qual a km da sua viagem: "))
if v > 200:
    print("Sua passagem fica no valor de R${:.2f}".format(v*0.45))
else:
    print("Sua passagem fica no valor de R${:.2f}".format(v*0.50))