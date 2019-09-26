numero1= (int)(input("Digite o primeiro numero: "))
numero2= (int)(input("Digite o segundo numero: "))

if numero1>numero2:
    print("A diferença de ",numero1, " para ", numero2, "eh", numero1-numero2)
elif numero2>numero1:
    print("A diferença de ",numero2, " para ", numero1, "eh", numero2-numero1)
else:
    print("Invalido!")