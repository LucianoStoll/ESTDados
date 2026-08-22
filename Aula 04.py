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
        pass

    def inserir_fim(self, valor):
        """Insere um novo elemento no final da lista (O(n))."""
        pass

    def buscar(self, valor) -> bool:
        """Retorna True se o valor estiver presente na lista, ou False caso contrário (O(n))."""
        pass

    def remover(self, valor) -> bool:
        """Remove a primeira ocorrência do valor na lista. Retorna True em caso de sucesso (O(n))."""
        pass

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