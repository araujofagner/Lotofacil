import random

def sorteio(lista = []):
    sorteados = []
    for item in lista:
        sorteados.append(item)
    
    while len(sorteados) < 15:
        ale = random.randint(1,25)
        
        if sorteados.count(ale) == 1:
            ale = random.randint(1,25)
        else:
            sorteados.append(ale)
    sorteados.sort()
    return sorteados

def jogar ():

    njogos = int (input("Quantos jogos você quer jogar? "))
    cercar = input ("Quer carcar algum número? ")
    ncercados = []
    lista = []

    if cercar == "S" or cercar == "s" or cercar == "Y" or cercar == "y":
        ncercar = int (input("Quantos números deseja cercar? "))
        for x in range(ncercar):
            ndigitado = int (input("Digite o número: "))
            ncercados.append(ndigitado)
        for item in ncercados:
            lista.append(item)
        
        for x in range(njogos):
            
            print(sorteio(lista))
    else:
        for x in range(njogos):
            
            print(sorteio(lista))
 
jogar()