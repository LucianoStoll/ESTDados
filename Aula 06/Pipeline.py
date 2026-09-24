# Objetivo: Praticar a manipulação de memória e ponteiros, convertendo e transformando uma mesma sequência de dados através das 4 estruturas vistas até agora: Vetor Estático, Lista Simplesmente Encadeada, Lista Duplamente Encadeada e Lista Circular.
# Visão Geral do Exercício

# Você recebe uma lista inicial de 10 números inteiros. O objetivo é fazer esses números passarem por quatro etapas consecutivas. A saída de uma etapa é a entrada da etapa seguinte:

 

# [Vetor Estático] 
#        ↓ (1. Filtra números ímpares deslocando na memória)
# [Lista Simplesmente Encadeada] 
#        ↓ (2. Inverte a ordem dos nós sem criar novos nós)
# [Lista Duplamente Encadeada] 
#        ↓ (3. Divide a lista exatamente na metade)
# [Lista Circular] 
#        ↓ (4. Elimina elementos dando saltos até restar 1)
# [Número Sobrevivente]

 
# As 4 Etapas da Atividade
# Etapa 1: Vetor Estático (Filtro por Deslocamento de Memória)

#     Entrada: Um array estático de tamanho fixo 10, preenchido com: [12, 7, 18, 9, 22, 15, 30, 41, 50, 3].

#     O que implementar:

#         remover_impares(): Percorrer o vetor e remover todos os números ímpares. Cada remoção exige deslocar (shift) todos os elementos à direita uma posição para a esquerda e diminuir o tamanho lógico.

#         exportar_para_lista_simples(): Criar e retornar uma nova Lista Simples contendo os elementos pares restantes na mesma ordem.

#     Saída esperada: Vetor com [12, 18, 22, 30, 50].

# Etapa 2: Lista Simplesmente Encadeada (Inversão In-Place de Ponteiros)

#     Entrada: A lista simplesmente encadeada gerada na Etapa 1 (12 -> 18 -> 22 -> 30 -> 50 -> None).

#     O que implementar:

#         inverter(): Inverter a direção da lista reorientando apenas os ponteiros .proximo dos nós existentes. É proibido criar novos nós ou copiar para listas auxiliares.

#         converter_para_dupla(): Percorrer a lista simples e criar uma Lista Duplamente Encadeada correspondente, configurando cabeca, cauda, proximo e anterior.

#     Saída esperada: Lista invertida: 50 -> 30 -> 22 -> 18 -> 12 -> None.

# Etapa 3: Lista Duplamente Encadeada (Divisão e Costura de Sublistas)

#     Entrada: A lista duplamente encadeada gerada na Etapa 2 (50 <-> 30 <-> 22 <-> 18 <-> 12).

#     O que implementar:

#         split_metade(): Dividir a lista ao meio. O método deve retornar duas listas duplas novas e independentes:

#             Metade 1: primeiros elementos (50 <-> 30 -> None).

#             Metade 2: elementos restantes (22 <-> 18 <-> 12 -> None).

#             Cada metade precisa ter suas próprias referências de cabeca e cauda válidas, com as pontas terminando em None.

#     Saída esperada: Duas listas duplas separadas.

# Etapa 4: Lista Circular (Fechamento de Ciclo e Eliminação por Saltos)

#     Entrada: A segunda metade obtida na Etapa 3 (22 <-> 18 <-> 12).

#     O que implementar:

#         fechar_ciclo(): Conectar a cauda de volta à cabeca (e o anterior da cabeça na cauda), transformando a estrutura em uma Lista Circular.

#         girar_e_eliminar(passos): A partir da cabeça, o algoritmo avança um número fixo de passos no anel, remove o nó onde parou (religando os vizinhos) e repete o processo até sobrar apenas um único nó.

#     Saída esperada: O valor do nó final sobrevivente (com passo = 2, o sobrevivente é o 22).

# =====================================================================
# DEFINIÇÃO DOS NÓS
# =====================================================================
class NodeSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


# =====================================================================
# 1. VETOR ESTÁTICO
# =====================================================================
class VetorEstatico:
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho = 0

    def inserir(self, valor) -> bool:
        if self.tamanho >= self.capacidade:
            return False
        self.dados[self.tamanho] = valor
        self.tamanho += 1
        return True

    def remover_impares(self):
        """Remove ímpares deslocando os elementos restantes à esquerda."""
        pass

    def exportar_para_lista_simples(self) -> 'ListaSimples':
        """Cria e retorna uma ListaSimples com os dados válidos do vetor."""
        pass

    def imprimir(self):
        print("Vetor:", [self.dados[i] for i in range(self.tamanho)])


# =====================================================================
# 2. LISTA SIMPLESMENTE ENCADEADA
# =====================================================================
class ListaSimples:
    def __init__(self):
        self.cabeca = None

    def inserir_fim(self, valor):
        """Insere um novo nó no final da lista simples."""
        pass

    def inverter(self):
        """Inverte a ordem dos nós in-place (reorientando apenas ponteiros .proximo)."""
        pass

    def converter_para_dupla(self) -> 'ListaDupla':
        """Cria e retorna uma ListaDupla com os elementos desta lista."""
        pass

    def imprimir(self):
        itens = []
        atual = self.cabeca
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        conteudo = " -> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Lista Simples: {conteudo}")


# =====================================================================
# 3. LISTA DUPLAMENTE ENCADEADA
# =====================================================================
class ListaDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def inserir_fim(self, valor):
        """Insere no fim amarrando .anterior, .proximo e atualizando self.cauda."""
        pass

    def split_metade(self):
        """
        Divide a lista ao meio.
        Retorna duas novas instâncias de ListaDupla: (metade1, metade2).
        """
        pass

    def imprimir_frente(self):
        itens = []
        atual = self.cabeca
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        conteudo = " <-> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Dupla Frente: {conteudo}")

    def imprimir_tras(self):
        itens = []
        atual = self.cauda
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.anterior
        conteudo = " <-> ".join(itens) + " -> None" if itens else "Vazia"
        print(f"Dupla Trás:   {conteudo}")


# =====================================================================
# 4. LISTA CIRCULAR (DUPLA)
# =====================================================================
class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    @classmethod
    def criar_a_partir_de_dupla(cls, lista_dupla: ListaDupla) -> 'ListaCircular':
        """Recebe uma ListaDupla e fecha o anel (cauda <-> cabeca)."""
        pass

    def girar_e_eliminar(self, passos: int) -> int:
        """
        A partir do nó atual, avança (passos - 1) vezes pelo ponteiro .proximo,
        remove o nó onde parou e religa os vizinhos no anel.
        O próximo ciclo recomeça a partir do nó seguinte ao removido.
        Repete até restar apenas 1 nó e retorna o seu dado.
        """
        pass

    def imprimir_uma_volta(self):
        if self.cabeca is None:
            print("Circular (1 volta): Vazia")
            return
        itens = []
        atual = self.cabeca
        for _ in range(self.tamanho):
            itens.append(str(atual.dado))
            atual = atual.proximo
        print("Circular (1 volta): " + " -> ".join(itens) + " -> [volta ao início]")


# =====================================================================
# EXECUÇÃO DE TESTE
# =====================================================================
if __name__ == "__main__":
    print("=== ETAPA 1: VETOR ESTÁTICO ===")
    v = VetorEstatico(10)
    for num in [12, 7, 18, 9, 22, 15, 30, 41, 50, 3]:
        v.inserir(num)
    v.imprimir()

    print("\nRemovendo ímpares:")
    v.remover_impares()
    v.imprimir()
    # Saída esperada: [12, 18, 22, 30, 50]

    print("\n=== ETAPA 2: LISTA SIMPLES ===")
    ls = v.exportar_para_lista_simples()
    ls.imprimir()
    # Saída esperada: 12 -> 18 -> 22 -> 30 -> 50 -> None

    print("\nInvertendo in-place:")
    ls.inverter()
    ls.imprimir()
    # Saída esperada: 50 -> 30 -> 22 -> 18 -> 12 -> None

    print("\n=== ETAPA 3: LISTA DUPLAMENTE ENCADEADA ===")
    ld = ls.converter_para_dupla()
    ld.imprimir_frente()
    ld.imprimir_tras()
    # Saída esperada (frente): 50 <-> 30 <-> 22 <-> 18 <-> 12 -> None

    print("\nDividindo ao meio:")
    m1, m2 = ld.split_metade()
    print("Metade 1:")
    m1.imprimir_frente()
    # Saída esperada: 50 <-> 30 -> None
    print("Metade 2:")
    m2.imprimir_frente()
    # Saída esperada: 22 <-> 18 <-> 12 -> None

    print("\n=== ETAPA 4: LISTA CIRCULAR & ELIMINAÇÃO ===")
    lc = ListaCircular.criar_a_partir_de_dupla(m2)
    lc.imprimir_uma_volta()
    # Saída esperada: 22 -> 18 -> 12 -> [volta ao início]

    print("\nEliminando com passo = 2:")
    sobrevivente = lc.girar_e_eliminar(passos=2)
    print(f"Elemento sobrevivente: {sobrevivente}")
    # Saída esperada: 12