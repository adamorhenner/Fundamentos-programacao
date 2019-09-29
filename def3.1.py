def soma(x,y):
    return x + y
x = (float)(input("Digite um valor x: "))
y = (float)(input("Digite um valor y: "))
soma = soma(x,y)
print(soma)

operacao = input("Qual operaçao? ")
if operacao == "+":
    print(soma)

def subtracao(x,y):
    return x - y
x = (float)(input("Digite um valor x: "))
y = (float)(input("Digite um valor y: "))
subtracao = subtracao(x,y)

operacao = input("Qual operaçao? ")
if operacao == "-":
    print(subtracao)
