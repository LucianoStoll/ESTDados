# =====================================================================
# 1. DEFINIÇÃO DO NÓ DUPLO (NODE DUPLO)
# =====================================================================
class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


# =====================================================================
# 2. DEFINIÇÃO DA LISTA DUPLAMENTE ENCADEADA (ESQUELETO)
# =====================================================================
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def esta_vazia(self) -> bool:
        pass

    def inserir_inicio(self, valor):
        pass

    def inserir_fim(self, valor):
        pass

    def imprimir_frente(self):
        pass

    def imprimir_tras(self):
        pass
