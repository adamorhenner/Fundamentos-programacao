#Escreva um programa em Python que leia dois números reais e que exiba o maior deles.
print("Digite dois numeros para saber qual é maior")
primeiro = (float)(input("Digite o primeiro numero: "))
segundo = (float)(input("Digite o segundo numero: "))
if primeiro>segundo:
    print("O numero ", primeiro, " eh maior")
else:
    print("O numero ", segundo, " eh maior")