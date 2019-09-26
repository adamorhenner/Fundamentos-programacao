print("=== Apto ou nao apto ===")
idade = (int)(input("Qual sua idade? "))
sexo = input("Qual seu sexo? ")
if idade>=18 and sexo == "masculino":
    print("APTO!")
else:
    print("Não APTO!")