#faça um programa que leia um conjunto de 10 numeros inteiros
#e ao final mostre qual foi o maior e o menor numero lido.
import math

menor = math.inf
maior = - math.inf

for i in range(10):

    numero = int(input("Digite um numero, por  farvor: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


print("O maior valor eh :", maior)
print("O menor valor eh :", menor)