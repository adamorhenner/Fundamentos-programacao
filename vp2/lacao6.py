controle = ""
estado = ""

while (controle != "x"):
    print("====================")
    print("Houve evolucao no processo? ")
    controle = input("Digite [S]  para sim, [N] para nao e [X] para sair: ")

    if controle == "s" :
        estado = input("Qual o novo estado? ")
        print("O estado atual do processo eh: ", estado)
    elif (estado == "n") :
        print(" :( ok")
    print("")

print("Estado final do processo: ", estado)
print("Ate a proxima")