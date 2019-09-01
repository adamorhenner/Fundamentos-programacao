ano = (int)(input("Qual seu ano ?"))
idade = 2019 - ano
print("Sua idade eh", idade, "anos")
if idade>=16 and idade>=18:
    print("Vc ja pode votar e dirigir")
elif idade>=16 and idade<18:
    print("nao pode dirigir, mas pode votar")
else:
    print("Voce não pode votar e nem dirigir")