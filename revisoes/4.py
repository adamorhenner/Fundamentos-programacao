print("Digite seu salario para saber o valor de imposto retido ")
salario=(float)(input("Informe seu salario: "))

if (salario <= 1566.61):
    print("Seu salario nao possui imposto retido")
elif salario <=2347.85:
    print((salario * 7.5)/100)
elif salario <=3130.51:
    print((salario * 15)/100)
elif salario <=3911.63:
    print((salario * 22.5)/100)
else:
    print((salario * 27.5)/100)