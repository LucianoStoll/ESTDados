class Node():
    def __init__(self, dado):
        self.dado = dado #Dado do nó
        self.proximo = None #Proximo nó


no1 = Node("A")
no2 = Node("B")
no3 = Node("C")
no4 = Node("D")

no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

primeiro = no1

while primeiro != None:
    print(primeiro.dado)
    primeiro = primeiro.proximo