print("==== Avalia se a area do triangulo eh menor do que 50 ====")
base = (int)(input("Qual a medida da base ?"))
altura = (int)(input("Qual a medida da Altura ?"))
area = base*altura/2
if area<50:
    print("A area eh menor que 50")
else:
    print("A area não eh menor que 50")