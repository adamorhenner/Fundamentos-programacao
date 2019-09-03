print("===Calculadora ===")
tipo = input("Informe se vc quer somar, multiplicar, diminuir ou dividir ")
numero = (float)(input("Digite um numero "))
otonumero = (float)(input("Digite outro numero "))

somar = numero + otonumero
multiplicar = numero*otonumero
diminuir = numero-otonumero
dividir = numero/otonumero
if tipo == "somar":
    print(somar)
elif tipo == "multiplicar":
    print(multiplicar)
elif tipo == "diminuir":
    print(diminuir)
elif tipo == "dividir":
    print(dividir)
else:
    print("erro")

#professor
print("==CALCULADORA===")

operador1 = (float)(input("Digite o primeiro operando: "))
operador2 = (float)(input("Digite o segundo operando: "))
operador = input("Digite qual operação quer realizar: ")

if (operador == "+"):
    print(operador1 + operador2)
elif (operador == "-"):
    print(operador1 - operador2)
elif (operador == "*"):
    print(operador1 * operador2)
elif (operador == "/"):
    if(operador2 == 0):
        print("Não eh possivel realizar divisao por zero")
    else:
        print(operador1 / operador2)
else:
    print("Operação invalida")
