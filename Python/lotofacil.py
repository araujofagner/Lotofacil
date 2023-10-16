import random

def sorteio(lista = []):
    sorteados = []
    for item in lista:
        sorteados.append(item)
    
    while len(sorteados) < 15:
        ale = random.randint(1,25)
        
        if sorteados.count(ale) == 1:
            sorteados.remove(ale)
        else:
            sorteados.append(ale)
    sorteados.sort()
    return sorteados

checa = []
print(sorteio(checa))