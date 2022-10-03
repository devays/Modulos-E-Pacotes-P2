def aumentar(valor = 0, porc = 0, set = False):
    porc = porc / 100
    total = valor * porc
    valor = valor + total 
    return valor if set is False else moeda(valor)

def reduzir(valor = 0,porc = 0, set = False):
    porc = porc / 100
    total = valor * porc
    valor = valor - total
    return valor if set is False else moeda(valor)


def metade(valor = 0, set = False):
    metade = valor / 2
    return metade if set is False else moeda(valor)

def dobro(valor = 0, set = False):
    dobro = valor * 2
    return dobro if set is False else moeda(valor)


def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')