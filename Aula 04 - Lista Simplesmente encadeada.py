# =====================================================================
# 1. DEFINIÇÃO DA ESTRUTURA DO NÓ (NODE)
# =====================================================================
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# =====================================================================
# 2. DEFINIÇÃO DA LISTA SIMPLESMENTE ENCADEADA
# =====================================================================
class ListaEncadeada:
    def __init__(self):
        """Inicializa uma lista encadeada vazia."""
        self.cabeca = None

    def esta_vazia(self) -> bool:
        """Verifica se a lista está vazia."""
        return self.cabeca is None

    def inserir_inicio(self, valor):
        """Insere um novo elemento no início da lista (O(1))."""
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_fim(self, valor):
        """Insere um novo elemento no final da lista (O(n))."""
        novo_no = Node(valor)
        if self.esta_vazia():
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def buscar(self, valor) -> bool:
        """Retorna True se o valor estiver presente na lista, ou False caso contrário (O(n))."""
        atual = self.cabeca
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor) -> bool:
        """Remove a primeira ocorrência do valor na lista. Retorna True em caso de sucesso (O(n))."""
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.dado == valor:
                if anterior is None:
                    # O elemento a remover é a cabeça da lista
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def __str__(self):
        """Retorna a representação visual da lista encadeada formatada em texto."""
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos) + " -> None" if elementos else "Lista Vazia"

# =====================================================================
# 3. BLOCO DE TESTES / DEMONSTRAÇÃO
# =====================================================================
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