n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 > n2 and n1 > n3:
    print("maior numero",n1)
elif n1 < n2 and n1 < n3:
    print("menor número",n1) 
if n2 > n3 and n2 > n1:
    print("maior numero",n2)
elif n2 < n1 and n2 < n3:
    print("menor número",n2)
if n3 > n2 and n3 > n1:
    print("maior numero",n3)
elif n3 < n2 and n3 < n1:
    print("menor número",n3)  
