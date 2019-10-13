# Escreva uma função que receba uma lista de inteiros
# de 16 posições e que retorne a soma dos quadrados
# dos números  ímpares contidos na lista
# Teste o funcionamento da funcao no final do codigo

soma = 0
for i in range (1,16):
    if i % 2 != 0:
        soma = soma + i
print (soma**2)