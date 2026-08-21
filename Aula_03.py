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

    def desengatar_vagao(primeiro_no, nome_alvo):
        atual = primeiro_no
        anterior = None

        while atual != None:
            if atual.nome == nome_alvo:
                if anterior is None:
                    return atual.proximo
                else:
                    anterior.proximo = atual.proximo
                    return primeiro_no

            anterior = atual
            atual = atual.proximo

    def inverter_trem(primeiro_no):
        anterior = None
        atual = primeiro_no

        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo

        return anterior

no1 = Node("Locomotiva", 80, None)
no2 = Node("Vagão Carga", 50, None)
no3 = Node("Vagão Passageiros", 30, None)
no4 = Node("Vagão Cauda", 10, None)
restaurante = Node("Vagão Restaurante", 25.0, None)

primeiro = no1

no1.proximo = no2
no2.proximo = restaurante
restaurante.proximo = no3
no3.proximo = no4

print(Node.relatorio_trem(no1))



print(Node.relatorio_trem(no1))

primeiro = Node.desengatar_vagao(no1, "Vagão Carga")

print(Node.relatorio_trem(no1))

primeiro = Node.inverter_trem(primeiro)
print(Node.relatorio_trem(primeiro))
