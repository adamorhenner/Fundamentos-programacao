print("===CONCEITO AMERICANO DE NOTAS===")
nota =(float) (input("Qual sua nota ?"))

if nota == 0.0 or nota<= 4.9:
    print("Sua nota eh conceito D")
elif nota== 5.0 or nota<=6.9:
    print("Sua nota eh conceito C")
elif nota==7.0 or nota<=8.9:
    print("Sua nota eh conceito B")
elif nota == 9.0 or nota<=10.0:
    print("Sua nota eh conceito A")