d = int(input("Quantos dia ficou alugado? "))
km = int(input("Quantos km foi percorrido na viagem? "))
pd = d * 60
pkm = km * 0.15
print("O preço de {} km rodados e {} dias alugados fica R${:.2f}".format(km, d, pd + pkm ))