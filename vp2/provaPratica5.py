#Esse programa recebe a idade do usuario e aplica desconto 
#numa lista de produtos de uma loja



def promocao(lista,idade) :
    for item in lista :
        desconto = item * idade
        item = item - desconto
        print(item)

print("Sua idade vale desconto nos nossos produtos, veja o preço dos produtos:")
produtos = [10,20,30,50,1000,80]
print(produtos)
idade = (int)(input("Qual sua idade? "))
idade = idade/100
print("VEJA QUANTO FICA NOSSOS PRODUTOS COM DESCONTO!!!!!!!")
promocao(produtos,idade)
print("O GERENTE FICOU MALUCO!!!")