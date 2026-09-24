# LISTA SIMPLESMENTE ENCADEADA — versão comentada para consulta.
# Node representa um elemento; ListaEncadeada gerencia a cabeça da corrente.
# self é a instância que recebeu a chamada: lista.buscar(10), por exemplo.
# -> bool é uma anotação de retorno; documenta o tipo, não força uma conversão.

class Node:
    def __init__(self, dado):
        self.dado = dado  # Conteúdo do elemento.
        self.proximo = None  # Último nó sempre aponta para None.


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Sem primeiro nó, a lista está vazia.

    def esta_vazia(self) -> bool:
        # O(1): basta consultar a cabeça; não precisamos contar nós.
        return self.cabeca is None

    def inserir_inicio(self, valor):
        novo_no = Node(valor)  # Aloca um novo elemento.
        # Liga à cabeça antiga ANTES de substituir a cabeça da lista.
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no  # Também funciona quando a cabeça antiga é None.

    def inserir_fim(self, valor):
        novo_no = Node(valor)
        if self.esta_vazia():
            self.cabeca = novo_no  # O primeiro nó também é o último.
            return  # Encerra para não tentar percorrer uma lista antes vazia.
        atual = self.cabeca  # Referência auxiliar preserva a cabeça.
        # Aqui queremos PARAR NO ÚLTIMO NÓ, não depois dele.
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no  # Engata o novo nó no fim.

    def buscar(self, valor) -> bool:
        atual = self.cabeca
        # Diferentemente de inserir_fim, precisamos examinar inclusive a cauda.
        while atual is not None:
            if atual.dado == valor:  # == compara conteúdo; = atribui.
                return True  # Encontrou: encerra a busca imediatamente.
            atual = atual.proximo
        return False  # Percorreu tudo sem encontrar (ou a lista estava vazia).

    def remover(self, valor) -> bool:
        atual = self.cabeca
        anterior = None  # A cabeça não tem antecessor.
        while atual is not None:
            if atual.dado == valor:
                if anterior is None:
                    self.cabeca = atual.proximo  # Remoção do primeiro nó.
                else:
                    # A -> B -> C vira A -> C ao remover B.
                    anterior.proximo = atual.proximo
                atual.proximo = None  # Desliga o nó retirado após religar a lista.
                return True  # Remove apenas a primeira ocorrência.
            anterior = atual  # Guarda o anterior antes de avançar atual.
            atual = atual.proximo
        return False  # Ausência do valor não altera a estrutura.

    def __str__(self):
        # print(lista) chama esta representação textual automaticamente.
        # A lista auxiliar abaixo só monta o texto; os dados continuam em nós.
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))  # join exige strings.
            atual = atual.proximo
        # join intercala a seta; lista vazia recebe uma mensagem específica.
        return " -> ".join(elementos) + " -> None" if elementos else "Lista Vazia"


# RESUMO: início O(1); fim O(n), pois não guardamos cauda; busca e remoção
# O(n) no pior caso. Conhecer o antecessor tornaria o ajuste da remoção O(1).
# __str__ usa O(n) de memória auxiliar para a representação textual.
# As inserções não têm return explícito: retornam None, mas alteram a lista.
# Não precisamos de global: os métodos atualizam atributos de self.
# O bloco abaixo só roda ao executar este arquivo diretamente.

if __name__ == "__main__":
    lista = ListaEncadeada()
    print("Estado inicial da lista:", lista)

    print("\n--- Testando inserir_fim ---")
    lista.inserir_fim(10)
    lista.inserir_fim(20)
    lista.inserir_fim(30)
    print("Lista após inserções no fim:", lista)

    print("\n--- Testando inserir_inicio ---")
    lista.inserir_inicio(5)
    print("Lista após inserção no início:", lista)

    print("\n--- Testando buscar ---")
    print("Buscar 20:", lista.buscar(20))
    print("Buscar 99:", lista.buscar(99))

    print("\n--- Testando remover ---")
    print("Remover 20:", lista.remover(20))
    print("Lista após remover 20:", lista)
    print("Remover 99 (inexistente):", lista.remover(99))

    print("\n--- Testando remover a cabeça ---")
    print("Remover 5:", lista.remover(5))
    print("Lista após remover 5:", lista)

    print("\n--- Testando esta_vazia ---")
    print("Lista está vazia?", lista.esta_vazia())