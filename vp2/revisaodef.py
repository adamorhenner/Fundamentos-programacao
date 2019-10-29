#escrever uma funcao que recebe um valor inteiro e exibe se o valor
#e positivo ou negativo
def positivoOuNegativo(valor):
    if valor > 0 :
        print("Positivo")
    elif valor < 0 :
        print("negativo")
    else :
        print("Nem chove nem molha")
numero = int(input("Digite um numero: "))

positivoOuNegativo(numero)
positivoOuNegativo(10)
positivoOuNegativo(-20)

repostaDoUsuario = (int)(input("Digite um valor e te direi seu sinal"))
positivoOuNegativo(repostaDoUsuario)