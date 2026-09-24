# =====================================================================
# 1. NÓ BÁSICO
# =====================================================================
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# =====================================================================
# 2. TAD PILHA (LIFO - Last In, First Out)
# =====================================================================
class Pilha:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """Retorna True se a pilha estiver vazia."""
        pass

    def tamanho(self) -> int:
        """Retorna a quantidade de elementos na pilha."""
        pass

    def push(self, valor):
        """Insere um novo nó no topo da pilha."""
        pass

    def pop(self):
        """Remove e retorna o valor do topo. Lança IndexError se vazia."""
        pass

    def peek(self):
        """Retorna o valor do topo sem remover. Lança IndexError se vazia."""
        pass

    def __repr__(self):
        itens = []
        atual = self._topo
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        return "Topo -> " + " -> ".join(itens) if itens else "Pilha Vazia"


# =====================================================================
# 3. TAD FILA (FIFO - First In, First Out)
# =====================================================================
class Fila:
    def __init__(self):
        self._frente = None
        self._fundo = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """Retorna True se a fila estiver vazia."""
        pass

    def tamanho(self) -> int:
        """Retorna a quantidade de elementos na fila."""
        pass

    def enqueue(self, valor):
        """Insere um novo nó no final (fundo) da fila."""
        pass

    def dequeue(self):
        """Remove e retorna o valor da frente. Lança IndexError se vazia."""
        pass

    def front(self):
        """Retorna o valor da frente sem remover. Lança IndexError se vazia."""
        pass

    def __repr__(self):
        itens = []
        atual = self._frente
        while atual is not None:
            itens.append(str(atual.dado))
            atual = atual.proximo
        return "Frente [" + " -> ".join(itens) + "] Fundo" if itens else "Fila Vazia"


# =====================================================================
# 4. DESAFIO PRÁTICO: BALANCEAMENTO DE DELIMITADORES
# =====================================================================
def verificar_delimitadores(expressao: str) -> bool:
    """
    Retorna True se os delimitadores (), [] e {} estiverem balanceados.
    Utiliza a classe Pilha para armazenar as aberturas.
    """
    pass


# =====================================================================
# EXECUÇÃO DE TESTES
# =====================================================================
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