Vet = []

def Add(a):
    Vet.append(a)


def Remover(a):
    if a in Vet:
        Vet.remove(a)

def BuscaInd(a):
    return Vet[a]

def BuscarVlr(a):
    if a in Vet:
        return Vet.index(a)






Add(10) #0
Add(20) #1
Add(30) #2
Add(40) #3
Add(50) #4

print(Vet)

print(BuscaInd(2))

print(BuscarVlr(10))

Remover(30)

print(Vet)





