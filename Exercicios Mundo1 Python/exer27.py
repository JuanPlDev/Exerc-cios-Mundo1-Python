n = input("Digite seu nome completo: ")
dividido = n.split()
print("Primeiro nome {}, último nome {} ".format(dividido[0], dividido[len(dividido) -1]))