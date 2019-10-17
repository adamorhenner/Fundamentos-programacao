# Escreva uma função que recebe uma lista com o
# preço de 10 produtos e que exibe os preços dos
# produtos reajustados em 15%
# Teste o funcionamento da funcao no final do codigo
#def reajusteProduto(produto):
#    print((produto *15)/ 100)

def reajustar(lista):
    for item in lista:
        reajuste = item + item * 0.15
        print(reajuste)

produtos = [100.0,2.0,3.0,400.00,5498.02,50.25,725.2,230.5,900.0,600.0]

reajustar(produtos)