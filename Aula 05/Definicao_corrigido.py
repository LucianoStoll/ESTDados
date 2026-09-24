# LISTA DUPLAMENTE ENCADEADA LINEAR — completa o esqueleto Definicao.py.
# Cada nó conhece o anterior e o próximo: podemos caminhar nos dois sentidos.
# Pontas: cabeca.anterior = None e cauda.proximo = None.
# Vazia: cabeca e cauda são None. Um só nó: ambas referenciam o mesmo objeto.

class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado  # Valor armazenado neste nó.
        self.anterior = None  # Referência para o vizinho à esquerda.
        self.proximo = None  # Referência para o vizinho à direita.


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None  # Entrada para percorrer de frente para trás.
        self.cauda = None  # Entrada para percorrer de trás para frente.

    def esta_vazia(self) -> bool:
        return self.cabeca is None  # Consulta direta: O(1).

    def inserir_inicio(self, valor):
        novo = NodeDuplo(valor)
        novo.proximo = self.cabeca  # Novo aponta para a antiga cabeça.
        if self.esta_vazia():
            self.cauda = novo  # Primeiro elemento também é o último.
        else:
            self.cabeca.anterior = novo  # Completa a ligação no sentido inverso.
        self.cabeca = novo  # Só então atualiza a entrada da lista.

    def inserir_fim(self, valor):
        novo = NodeDuplo(valor)
        novo.anterior = self.cauda  # Novo aponta para a antiga cauda.
        if self.esta_vazia():
            self.cabeca = novo  # Caso especial: a lista não tinha nenhum nó.
        else:
            self.cauda.proximo = novo  # Antiga cauda aponta para o novo nó.
        self.cauda = novo  # Não precisamos percorrer: guardamos a cauda!

    def imprimir_frente(self):
        atual = self.cabeca  # Começa no primeiro.
        while atual is not None:
            print(atual.dado, end=" <-> ")  # end mantém a saída na mesma linha.
            atual = atual.proximo  # Segue para a direita.
        print("None")  # Também representa corretamente a lista vazia.

    def imprimir_tras(self):
        atual = self.cauda  # Começa no último.
        while atual is not None:
            print(atual.dado, end=" <-> ")
            atual = atual.anterior  # Segue para a esquerda.
        print("None")


# RESUMO: inserções em ambas as pontas O(1); impressão O(n).
# O preço de poder voltar é uma referência adicional por nó.
# Esquecer uma das ligações pode fazer a leitura para frente funcionar
# e a leitura para trás falhar: sempre confira os DOIS sentidos.
# Execute Bloco_de_Testes_corrigido.py, na mesma pasta, para ver os exemplos.
