#função retorna o valor com o desconto de 15%
def calculaDesconto(v):
    valor = v
    desconto = valor *(15/100)
    valor -= desconto
    return valor


