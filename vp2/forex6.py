# Escreva uma função que recebe uma lista com o
# preço de 10 produtos e que exibe os preços dos
# produtos reajustados em 15%
# Teste o funcionamento da funcao no final do codigo
#def reajusteProduto(produto):
#    print((produto *15)/ 100)

def reajustar(produto):
    novoPreco = produto + produto * 0.15
    print(novoPreco)


for i in range(10):
    feijao = 10
    input("qual o produto? ")
    
    
    reajustar(feijao)

