print("Calcular o valor de hora trabalhada")
horas_trab= (float)(input("Quantas horas trabalhada? "))
valor_hora = (float)(input("Quanto recebe por hora trabalhada? "))
desconto = (float)(input("Informe o valor do desconto do IR: "))

salario_bruto = horas_trab*valor_hora

salario_liquido = salario_bruto - (salario_bruto*(desconto/100))

print("Seu salario liquido eh igual a", salario_liquido)