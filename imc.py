def saude(altura,peso):
    imc = peso/(altura*2)

    if imc <= 18.5 :
        print("abaixo do peso ")
    elif imc <= 24.9 :
        print("peso normal")
    elif imc <= 29.9 :
        print("sobrepeso")
    elif imc <= 34.9 :
        print("obesidade grau 1")
    elif imc <= 39.9 :
        print("obesidade grau 2")
    elif imc <= 40 :
        print("obesidade grau 3")


peso = float(input("Qual seu peso? "))
altura = float (input("Qual sua altura? "))
imc = saude(altura, peso)

