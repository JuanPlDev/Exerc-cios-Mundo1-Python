s = float(input("Qual o valor do salário: "))
if s > 1250:
    print("O salário com aumento fica R${:.2f}".format(s + s/100*10))
elif s <= 1250:
    print("O salário com aumento fica R${:.2f}".format(s + s/100*15)) 
