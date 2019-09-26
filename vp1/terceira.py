salario = (float)(input("Informe seu salario: "))

if salario <= 1800:
    print ("Seu salario de R$",salario,", pertence a FAIXA 1, com juros a 0%")
elif salario <= 2600:
    print ("Seu salario de R$",salario,", pertence a FAIXA 1,5 com juros a 5%, que eh igual a : R$", (salario*5)/100, "Reais de juros")
elif salario <= 3000:
    print ("Seu salario de R$",salario,", pertence a FAIXA 2 com juros a 6%, que eh igual a : R$", (salario*6)/100, "Reais de juros")
elif salario <= 4000:
    print ("Seu salario de R$",salario,", pertence a FAIXA 2 com juros a 7%, que eh igual a : R$", (salario*7)/100, "Reais de juros")
elif salario <= 7000:
    print ("Seu salario de R$",salario,", pertence a FAIXA 3 com juros a 8.16%, que eh igual a : R$", (salario*8.16)/100, "Reais de juros")
elif salario <= 9000:
    print ("Seu salario de R$",salario,", pertence a FAIXA 3 com juros a 9.16%, que eh igual a : R$", (salario*9.16)/100, "Reais de juros")