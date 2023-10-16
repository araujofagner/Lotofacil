import random

def sorteio():
    sorteados = []
    while len(sorteados) < 15:
        ale = random.randint(1,25)
        
        if sorteados.count(ale) == 1:
            sorteados.remove(ale)
        else:
            sorteados.append(ale)
    return sorteados

resultado = sorteio()
resultado.sort()
print(resultado)