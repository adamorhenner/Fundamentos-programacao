#Escreva um programa em Python que lê um caractere e que caso o usuário entre com ‘a’ escreva na tela “Primeira letra do Alfabeto” e que caso o usuário entre com ‘z’ escreva na tela “Última letra do alfabeto”. Caso contrário escreva "Opção inválida".
print("Informe letra 'a' ou 'z'")
caractere = input("Digite uma letra: ")
if caractere == "a":
    print("Primeira letra do Alfabeto")
elif caractere == "z":
    print("Ultima letra do Alfabeto")
else:
    print("Opção inválida")
