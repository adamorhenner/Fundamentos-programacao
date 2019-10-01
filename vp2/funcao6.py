def soma(x , y):
    print(x + y)
def subtracao(x , y):
    print(x - y)
def multiplicacao(x , y):
    print(x * y)
def divisao(x , y):
    if (y == 0):
        print("Nao eh possivel realizar divisao por Zero")
    else:
        print(x / y)
def calcular(tipo, x, y):
    if (tipo == "+"):
        soma(x, y)
    elif (tipo == "-"):
        subtracao(x, y)
    elif (tipo == "*"):
        multiplicacao(x, y)
    elif (tipo == "/"):
        divisao(x, y)
    else:
        print("Operacao invalida")






operando1 = (float) (input("Digite o primeiro operando: "))
operando2 = (float) (input("Digite o segundo operando: "))
operador = input("Digite qual operacao quer realizar: ")

calcular(operador, operando1, operando2)