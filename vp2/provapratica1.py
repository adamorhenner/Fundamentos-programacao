pergunta = input("impar ou par? ")

if pergunta == "par":
    for par in range (0,101):
        if par % 2 == 0:
            print(par)
elif pergunta == "impar":
    for impar in range (100):
        if impar % 2 != 0:
            print(impar)
else:
    print("ERRO, Escreva 'par' ou 'impar'")
