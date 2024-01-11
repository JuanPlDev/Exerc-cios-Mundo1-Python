n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite segundo numero: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, \n o produto é {}, a divisão é {:.3f}".format(s, m, d), end=" >>> " )
print("A divisão inteira é {} e a potência é {}".format(di, e))