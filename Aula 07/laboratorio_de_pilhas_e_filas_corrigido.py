# PILHA E FILA ENCADEADAS — métodos completos e explicados.
# Pilha: LIFO, último a entrar é o primeiro a sair (como pratos empilhados).
# Fila: FIFO, primeiro a entrar é o primeiro a sair (como uma fila de atendimento).
# O prefixo _ indica atributo de uso interno por convenção, não proteção real.
# self é o objeto que recebeu a chamada; -> bool/int documenta o tipo de retorno.

class Node:
    def __init__(self, dado):
        self.dado = dado  # Conteúdo armazenado.
        self.proximo = None  # Ligação com o nó seguinte.


class Pilha:
    def __init__(self):
        self._topo = None  # Todas as inserções e remoções acontecem aqui.
        self._tamanho = 0  # Contador evita percorrer a estrutura para contar.

    def esta_vazia(self) -> bool:
        return self._topo is None  # Sem topo, não existe elemento.

    def tamanho(self) -> int:
        return self._tamanho  # Consulta O(1).

    def push(self, valor):
        novo = Node(valor)
        novo.proximo = self._topo  # Novo preserva o acesso ao antigo topo.
        self._topo = novo  # Último inserido passa a ser o primeiro a sair.
        self._tamanho += 1

    def pop(self):
        if self.esta_vazia():
            # O enunciado exige erro: None não distinguiria vazio de dado None.
            raise IndexError("Não é possível remover de uma pilha vazia.")
        removido = self._topo  # Guarda o nó para devolver seu conteúdo.
        self._topo = removido.proximo  # O segundo nó vira o topo (ou None).
        removido.proximo = None  # Desliga o nó removido.
        self._tamanho -= 1
        return removido.dado  # Retorna o valor, não o objeto Node.

    def peek(self):
        if self.esta_vazia():
            raise IndexError("Não existe topo em uma pilha vazia.")
        return self._topo.dado  # Apenas consulta: não altera ligações nem tamanho.

    def __repr__(self):
        # Representação usada para visualizar a instância; deve retornar string.
        itens = []  # Auxiliar só para montar o texto, não para implementar a pilha.
        atual = self._topo
        while atual is not None:
            itens.append(str(atual.dado))  # str converte o valor para texto.
            atual = atual.proximo
        return "Topo -> " + " -> ".join(itens) if itens else "Pilha Vazia"


class Fila:
    def __init__(self):
        self._frente = None  # Próximo elemento a sair.
        self._fundo = None  # Ponto de entrada dos novos elementos.
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        return self._frente is None

    def tamanho(self) -> int:
        return self._tamanho

    def enqueue(self, valor):
        novo = Node(valor)
        if self.esta_vazia():
            self._frente = novo  # Primeiro nó é frente e fundo ao mesmo tempo.
        else:
            self._fundo.proximo = novo  # Engata após quem já estava esperando.
        self._fundo = novo  # Guardar o fundo evita uma varredura O(n).
        self._tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma fila vazia.")
        removido = self._frente
        self._frente = removido.proximo  # O segundo da fila vira o primeiro.
        if self._frente is None:
            self._fundo = None  # Saiu o último: AMBAS as pontas devem ficar vazias.
        removido.proximo = None
        self._tamanho -= 1
        return removido.dado

    def front(self):
        if self.esta_vazia():
            raise IndexError("Não existe frente em uma fila vazia.")
        return self._frente.dado  # Consulta sem atender/remover o elemento.

    def __repr__(self):
        itens = []
        atual = self._frente
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        return "Frente [" + " -> ".join(itens) + "] Fundo" if itens else "Fila Vazia"


def verificar_delimitadores(expressao: str) -> bool:
    # A abertura mais recente deve ser fechada primeiro: exatamente LIFO.
    # Apenas contar aberturas e fechamentos não basta: ([)] teria contagens
    # iguais, mas fecha o parêntese antes de fechar o colchete interno.
    pilha = Pilha()
    for caractere in expressao:  # Examina cada caractere uma vez.
        if caractere in "([{":
            pilha.push(caractere)  # Guarda a abertura que espera fechamento.
        elif caractere in ")]}":
            if pilha.esta_vazia():
                return False  # Fechamento sem abertura correspondente.
            abertura = pilha.pop()  # Deve combinar com a abertura mais recente.
            if (caractere == ")" and abertura != "(") or \
               (caractere == "]" and abertura != "[") or \
               (caractere == "}" and abertura != "{"):
                return False  # Tipos diferentes ou ordem de fechamento inválida.
        # Letras, espaços e operadores são ignorados por este exercício.
        # Não é um analisador de linguagem: delimitadores em strings/comentários
        # também são contados, pois não tratamos sintaxe de código-fonte.
    # Se sobraram aberturas, faltaram fechamentos. Expressão vazia é balanceada.
    return pilha.esta_vazia()


# SIMULAÇÃO PARA "([])":
# '(' -> empilha '('; '[' -> empilha '['; ']' -> desempilha '[' e combina;
# ')' -> desempilha '(' e combina; termina vazia, portanto True.
#
# RESUMO: push/pop/peek, enqueue/dequeue/front, tamanho e esta_vazia são O(1).
# __repr__ percorre n nós e monta texto: O(n) tempo e espaço auxiliar.
# Verificar delimitadores: O(n) tempo e O(n) espaço no pior caso (só aberturas).
# push/enqueue alteram a estrutura e retornam None implicitamente.
# pop/dequeue alteram e retornam um valor; peek/front apenas consultam.
# Os exemplos abaixo testam LIFO, FIFO e expressões válidas e inválidas.

if __name__ == "__main__":
    print("=== ETAPA 1: TESTANDO A PILHA (LIFO) ===")
    p = Pilha()
    print("Pilha inicial:", p)
    print("Está vazia?", p.esta_vazia())

    print("\nEmpilhando 6 valores:")
    valores_pilha = [10, 20, 30, 40, 50, 60]
    for val in valores_pilha:
        p.push(val)
        print(f"push({val}) -> {p}")

    print("\nConsultas:")
    print("Tamanho atual:", p.tamanho())
    print("Peek (topo):", p.peek())

    print("\nDesempilhando 3 elementos:")
    for _ in range(3):
        print(f"pop() -> removeu: {p.pop()} | Restante: {p}")

    print("\nEmpilhando mais 2 valores (70 e 80):")
    p.push(70)
    p.push(80)
    print("Pilha após novas entradas:", p)

    print("\nEsvaziando o restante da pilha:")
    while not p.esta_vazia():
        print(f"pop() -> {p.pop()} | Pilha: {p}")

    print("Está vazia agora?", p.esta_vazia())


    print("\n=== ETAPA 2: TESTANDO A FILA (FIFO) ===")
    f = Fila()
    print("Fila inicial:", f)
    print("Está vazia?", f.esta_vazia())

    print("\nEnfileirando 6 atendimentos:")
    processos = ["Proc_1", "Proc_2", "Proc_3", "Proc_4", "Proc_5", "Proc_6"]
    for proc in processos:
        f.enqueue(proc)
        print(f"enqueue('{proc}') -> {f}")

    print("\nConsultas:")
    print("Tamanho atual:", f.tamanho())
    print("Front (próximo da frente):", f.front())

    print("\nAtendendo 3 processos (dequeue):")
    for _ in range(3):
        print(f"dequeue() -> atendeu: {f.dequeue()} | Fila restante: {f}")

    print("\nChegando mais 2 processos (Proc_7 e Proc_8):")
    f.enqueue("Proc_7")
    f.enqueue("Proc_8")
    print("Fila após novas entradas:", f)

    print("\nAtendendo todos os processos restantes:")
    while not f.esta_vazia():
        print(f"dequeue() -> atendeu: {f.dequeue()} | Fila: {f}")

    print("Está vazia agora?", f.esta_vazia())


    print("\n=== ETAPA 3: TESTANDO O BALANCEAMENTO ===")
    casos = [
        "()",
        "([]){}",
        "((([[[{{{}}}]]])))",
        "int x = (a[0] + b[1]) * {c + (d * e)};",
        "(",
        ")",
        "(]",
        "([)]",
        "(()",
        "func(x[0} + y)"
    ]

    for expr in casos:
        resultado = verificar_delimitadores(expr)
        print(f"{expr:<42} -> {resultado}")