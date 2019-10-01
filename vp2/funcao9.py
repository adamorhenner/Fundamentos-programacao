def reajustar(salarioAtual):
    novoSalario = salarioAtual + salarioAtual * 0.15
    return novoSalario



print("===== Aumento seu salario =====")

salario = (float)(input("Qual valor do seu salario ?"))
salarioReajustado = reajustar(salario)
#incrementando:
#salario += salario * 0.15

print("O valor do seu salario reajustado em 15% eh:", salarioReajustado)