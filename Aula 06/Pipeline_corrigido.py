# PIPELINE: vetor -> lista simples -> lista dupla -> lista circular.
# Cada etapa usa a saída da anterior. As conversões criam nós quando permitido;
# inverter e dividir reaproveitam os nós existentes, ajustando referências.
#
# CONTRADIÇÃO NO ORIGINAL: a descrição inicial diz sobrevivente 22, mas
# o método detalha avançar passos - 1 vezes e o teste final espera 12.
# Seguimos o método detalhado: conta o nó atual como 1. Com [22, 18, 12]
# e passos=2, remove 18, depois 22, sobrando 12.
#
# Convenções: self é a instância; None significa ausência de nó;
# -> 'ListaSimples' é uma anotação de tipo em texto, permitindo citar uma
# classe que ainda será definida. Anotações não verificam tipos em execução.

class NodeSimples:
    def __init__(self, dado):
        self.dado = dado  # Conteúdo do nó.
        self.proximo = None  # Ligação de ida.


class NodeDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None  # Ligação de volta, extra em relação ao nó simples.
        self.proximo = None


class VetorEstatico:
    def __init__(self, capacidade=10):
        if capacidade < 0:
            raise ValueError("A capacidade não pode ser negativa.")
        self.capacidade = capacidade  # Limite fixo de elementos.
        self.dados = [None] * capacidade  # Reserva as posições uma única vez.
        self.tamanho = 0  # Conta somente as posições ocupadas.

    def inserir(self, valor) -> bool:
        if self.tamanho >= self.capacidade:
            return False  # Impede escrever fora do vetor.
        self.dados[self.tamanho] = valor  # tamanho é a primeira posição livre.
        self.tamanho += 1  # Atualiza só após armazenar o valor.
        return True

    def remover_impares(self):
        indice = 0  # Começa no primeiro elemento válido.
        while indice < self.tamanho:
            # % calcula o resto: um inteiro é ímpar quando o resto por 2 não é 0.
            if self.dados[indice] % 2 != 0:
                # Desloca todos os elementos à direita uma posição à esquerda.
                for posicao in range(indice, self.tamanho - 1):
                    self.dados[posicao] = self.dados[posicao + 1]
                self.tamanho -= 1  # A capacidade física permanece igual.
                self.dados[self.tamanho] = None  # Limpa a antiga última posição.
                # NÃO avança indice: o elemento que veio da direita ainda
                # precisa ser examinado. Isso trata ímpares consecutivos.
            else:
                indice += 1  # Só avança quando o elemento atual deve permanecer.

    def exportar_para_lista_simples(self) -> 'ListaSimples':
        lista = ListaSimples()  # A nova estrutura é independente do vetor.
        for indice in range(self.tamanho):  # Ignora posições livres.
            lista.inserir_fim(self.dados[indice])  # Preserva a ordem dos valores.
        return lista

    def imprimir(self):
        # A compreensão gera apenas uma lista temporária para exibir os válidos.
        print("Vetor:", [self.dados[i] for i in range(self.tamanho)])


class ListaSimples:
    def __init__(self):
        self.cabeca = None

    def inserir_fim(self, valor):
        novo = NodeSimples(valor)
        if self.cabeca is None:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.proximo is not None:  # Para no último nó, não em None.
            atual = atual.proximo
        atual.proximo = novo

    def inverter(self):
        anterior = None  # Parte já invertida, inicialmente vazia.
        atual = self.cabeca
        while atual is not None:
            proximo = atual.proximo  # 1. Salva o caminho antes de apagá-lo.
            atual.proximo = anterior  # 2. Inverte a seta.
            anterior = atual  # 3. Aumenta a parte invertida.
            atual = proximo  # 4. Continua pelo caminho salvo.
        self.cabeca = anterior  # A antiga cauda virou a cabeça.

    def converter_para_dupla(self) -> 'ListaDupla':
        lista = ListaDupla()
        atual = self.cabeca
        while atual is not None:
            # Aqui é permitido criar nós: a restrição era para inverter.
            lista.inserir_fim(atual.dado)
            atual = atual.proximo
        return lista

    def imprimir(self):
        atual = self.cabeca  # Auxiliar: não modifica a cabeça.
        print("Lista Simples: ", end="")
        while atual is not None:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


class ListaDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None  # Permite inserir no fim sem percorrer a lista.
        self.tamanho = 0

    def inserir_fim(self, valor):
        novo = NodeDuplo(valor)
        novo.anterior = self.cauda
        if self.cabeca is None:
            self.cabeca = novo  # Primeiro elemento é cabeça e cauda.
        else:
            self.cauda.proximo = novo  # Completa a ligação entre os vizinhos.
        self.cauda = novo
        self.tamanho += 1

    def split_metade(self):
        # Cria dois gerenciadores, mas NÃO copia os nós.
        metade1 = ListaDupla()
        metade2 = ListaDupla()
        corte = self.tamanho // 2  # Divisão inteira: 5 // 2 = 2.
        # Para tamanho ímpar, a segunda metade recebe o elemento extra.
        metade1.tamanho = corte
        metade2.tamanho = self.tamanho - corte
        if corte == 0:
            # Lista vazia ou unitária: a primeira metade fica vazia.
            metade2.cabeca = self.cabeca
            metade2.cauda = self.cauda
        else:
            fim_primeira = self.cabeca
            for _ in range(corte - 1):  # Já estamos no primeiro: anda corte - 1.
                fim_primeira = fim_primeira.proximo
            metade1.cabeca = self.cabeca
            metade1.cauda = fim_primeira
            metade2.cabeca = fim_primeira.proximo  # Salva antes de cortar.
            metade2.cauda = self.cauda
            metade1.cauda.proximo = None  # Corta a ligação de ida.
            metade2.cabeca.anterior = None  # Corta também a ligação de volta.
        # Transferimos os nós para as metades. Esvaziar o gerenciador antigo
        # evita que ele mantenha cabeça/cauda/tamanho incompatíveis após o corte.
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        return metade1, metade2  # Tupla de dois gerenciadores, não cópia dos nós.

    def imprimir_frente(self):
        atual = self.cabeca
        print("Dupla Frente: ", end="")
        while atual is not None:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

    def imprimir_tras(self):
        atual = self.cauda  # A leitura inversa começa no outro extremo.
        print("Dupla Trás: ", end="")
        while atual is not None:
            print(atual.dado, end=" <-> ")
            atual = atual.anterior
        print("None")


class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def fechar_ciclo(self):
        # Converte as pontas abertas em um anel fechado, se existir algum nó.
        if self.cabeca is not None:
            self.cauda.proximo = self.cabeca
            self.cabeca.anterior = self.cauda

    @classmethod
    def criar_a_partir_de_dupla(cls, lista_dupla: ListaDupla) -> 'ListaCircular':
        # @classmethod recebe a CLASSE em cls, em vez de uma instância em self.
        circular = cls()  # Cria um gerenciador circular vazio.
        circular.cabeca = lista_dupla.cabeca  # Transfere os nós sem copiá-los.
        circular.cauda = lista_dupla.cauda
        circular.tamanho = lista_dupla.tamanho
        circular.fechar_ciclo()
        # A origem deixa de possuir os nós: imprimir como lista linear após
        # fechar o anel provocaria um laço sem fim se mantivéssemos as referências.
        lista_dupla.cabeca = None
        lista_dupla.cauda = None
        lista_dupla.tamanho = 0
        return circular

    def girar_e_eliminar(self, passos: int) -> int:
        if not isinstance(passos, int) or isinstance(passos, bool) or passos < 1:
            raise ValueError("Passos deve ser um inteiro positivo.")
        if self.cabeca is None:
            raise ValueError("Não existe sobrevivente em uma lista vazia.")
        atual = self.cabeca
        while self.tamanho > 1:
            # Conta o nó atual como 1; por isso avança passos - 1 ligações.
            for _ in range(passos - 1):
                atual = atual.proximo
            seguinte = atual.proximo  # A próxima contagem começa no sucessor.
            atual.anterior.proximo = seguinte  # Vizinho esquerdo pula o alvo.
            seguinte.anterior = atual.anterior  # Repara a ligação de volta.
            if atual is self.cabeca:
                self.cabeca = seguinte
            if atual is self.cauda:
                self.cauda = atual.anterior
            atual.proximo = None  # Desliga o retirado só depois de religar vizinhos.
            atual.anterior = None
            self.tamanho -= 1
            atual = seguinte
        # O único nó restante aponta para si mesmo e é cabeça e cauda.
        return self.cabeca.dado

    def imprimir_uma_volta(self):
        if self.cabeca is None:
            print("Circular (1 volta): Vazia")
            return
        atual = self.cabeca
        print("Circular (1 volta): ", end="")
        # Como sabemos o tamanho, visitar essa quantidade impede voltas infinitas.
        for _ in range(self.tamanho):
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("[volta ao início]")


# RESUMO DE CUSTOS (n = elementos na etapa; p = passos):
# Remover ímpares por deslocamentos: O(n²) no pior caso, como pede o exercício.
# Exportar para simples: O(n²) aqui, pois inserir_fim percorre a lista a cada vez.
# Inverter: O(n) tempo, O(1) espaço auxiliar, sem criar nós.
# Converter para dupla: O(n), pois a dupla guarda a cauda e insere em O(1).
# Dividir: O(n) tempo; cria só dois gerenciadores e reaproveita os nós.
# Fechar ciclo: O(1). Eliminar: O(n*p); para p fixo, O(n).
# Ao dividir e circularizar, a estrutura de origem fica vazia por transferência.
# O bloco abaixo mostra as saídas esperadas de cada etapa.

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