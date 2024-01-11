a = float(input("Qual a altura da parede: "))
l = float(input("Qual a largura da parede: "))
area = a * l
tinta = area / 2
print("A sua parede tem a dimensão de {}x{} e sua aréa é {}m²".format(a, l, area))
print("Para pintar essa parede voce vai precisar de {}L de tinta".format(tinta))
