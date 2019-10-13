# faça um programa utilizando o for
# que apresente a tabuada de um inteiro informado
# pelo o usuário
#tabuada = [0,1,2,3,4,5,6,7,8,9,10]
#for numero in tabuada:
##    inteiro = (int)(input("informe um numero; "))

operacao = input("Digite a operação desejada +, -, *, /: ")
if operacao == "+":
    numeroo= (int)(input("digite numero: "))
    for i in range(10):
        soma = i + numeroo
        print(i,"+", numeroo, "=", soma)
elif operacao == "-" :
    numeroo= (int)(input("digite numero: "))
    for i in range(10):
        soma = numeroo - i
        print(numeroo, "-", i ,"=", soma)
elif operacao == "*" :
    numeroo= (int)(input("digite numero: "))
    for i in range(11):
        soma = numeroo * i
        print(numeroo, "*", i ,"=", soma)
elif operacao == "/" :
    numeroo= (int)(input("digite numero: "))
    for i in range(1,10):
        soma = numeroo / i
        print(numeroo, "/", i ,"=", soma)