operacao= input("Digite a operação: ")

if operacao == "+":
    def soma(x,y):
        return x + y
    x = (float)(input("Digite um valor x: "))
    y = (float)(input("Digite um valor y: "))
    print(soma(x,y))
elif operacao == "-":
    def subtracao(x,y):
        return x - y
    x = (float)(input("Digite um valor x: "))
    y = (float)(input("Digite um valor y: "))
    print(subtracao(x,y))
elif operacao == "*":
    def multiplicacao(x,y):
        return x * y
    x = (float)(input("Digite um valor x: "))
    y = (float)(input("Digite um valor y: "))
    print(multiplicacao(x,y))
elif operacao == "/":
    def divisao(x,y):
        return x / y
    x = (float)(input("Digite um valor x: "))
    y = (float)(input("Digite um valor y: "))
    print(divisao(x,y))
else:
    print("ERRO, DIGITE A OPERAÇÃO DESEJADA : + -  *  /")