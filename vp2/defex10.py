def aumento(salario):
    return (salario * 1.15)

print("===== Aumento seu salario =====")
salario = (float)(input("Qual valor do seu salario ?"))
salario = aumento(salario)
#incrementando:
#salario += salario * 0.15

print("O valor do seu salario reajustado em 15% eh:", salario)
