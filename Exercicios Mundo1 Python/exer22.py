n = input("Digite seu nome: ")
print(n.upper())
print(n.lower())
s = n.split()
e = ''.join(s)
print("A quantidade de letras desconsiderando os espaços é ",len(e))
qtdpnome = s [0]
print("A quantidade de letras do primeiro nome é ",len(qtdpnome))