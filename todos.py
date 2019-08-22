nome = input("Qual seu nome ?")
print("Olá"+nome+ ",seja bem vindo!")

print(nome + ", Informe sua data de nascimento :")
Dia = input("Qual o dia ?")
Mes = input("De que mês ?")
Ano = input("E de qual ano ?")
Idade = (2019 - (int) (Ano)) 
print("Você nasceu em " +Dia+"/"+Mes+"/"+Ano+ " Sua idade eh", Idade ,"Anos" )



print("digite dois numero e exibirei a soma ")
Primeiro = (float)(input("Digite o primeiro numero: "))
segundo = (float)(input("Digite o segundo numero: "))
print(Primeiro+segundo)

print("Digite um numero e exibirei o dobro")
numero = (int)(input("Qual numero?"))
dobro = 2* (int)(numero)
print ("O dobro eh", dobro)

print("Me informe suas notas e calcularei sua media")
vp1 = (float)(input ("Qual sua vp1 ?"))
vp2 = (float)(input ("Qual sua vp2 ?"))
vpf = (float)(input ("Qual sua vpf ?"))
media = (vp1+2*vp2+3*vpf)/6
print("Sua media é", media)