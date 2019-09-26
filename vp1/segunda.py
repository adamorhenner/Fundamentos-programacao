opção = input("Voce deseja realizar operação de potencia ou de raiz? ")

if opção=="potencia":
    numero = (int)(input("Digite um valor: "))
    potencia = (int)(input("Informe uma potencia: "))
    print("Potencia de ",numero,"Elevado a ",potencia," eh ",numero**potencia)
elif opção=="raiz":
    numero = (int)(input("Digite um valor: "))
    raiz = (int)(input("Informe a raiz: "))
    print("a raiz",raiz," de ", numero, " eh ", numero**(1/raiz))
else:
    print("Operação invalida, digite 'potencia' ou 'raiz'")