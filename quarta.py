x = (float)(input("Qual angulo de x ? "))
y = (float)(input("Qual angulo de y ? "))
z = (float)(input("Qual angulo de z ? "))

if x == 90 and y<90 and z<90:
    print("Eh um triangulo retangulo")
elif x<90 and y ==90 and z<90:
    print("Eh um triangulo retangulo")
elif x<90 and y<90 and z == 90:
    print("Eh um triangulo retangulo")
else:
    print("Não eh um triangulo retangulo")
