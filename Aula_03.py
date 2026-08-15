class Node():
    def __init__(self, nome, peso, proximo):
        self.nome = nome
        self.peso = peso
        self.proximo = None

    def relatorio_trem(primeiro):
        atual = primeiro
        Peso = 0
        Qtd = 0



        while atual != None:
            Peso += atual.peso
            Qtd += 1


            print(f"[ {atual.nome}] ({atual.peso}) --> ")

            if atual == None:
                print("Fim")

            atual = atual.proximo

        print(f"Peso total do trem: {Peso}")
        print(f"Quantidade de vagões: {Qtd}")
            

no1 = Node("Locomotiva", 80, None)
no2 = Node("Vagão Carga", 50, None)
no3 = Node("Vagão Passageiros", 30, None)
no4 = Node("Vagão Cauda", 10, None)

primeiro = no1

no1.proximo = no2
no2.proximo = no3
no3.proximo = no4

print(Node.relatorio_trem(primeiro))


