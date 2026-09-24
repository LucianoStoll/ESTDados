# Avaliação de Estrutura de Dados — Gabarito comentado

**Curso:** Sistemas • **Conteúdo:** Aulas 01 a 07 • **Valor:** 10,0 pontos  
**Formato:** 10 questões de 1,0 ponto • **Tempo sugerido para simulação:** 180 minutos  
**Modalidade:** individual, com consulta aos códigos e às anotações.

Avaliação de estudo elaborada a partir dos enunciados TXT, exercícios Python e versões comentadas da pasta. Reproduz o formato de questões conceituais, implementação por requisitos, simulação de cenários e análise de resultados das atividades. Os PDFs não foram usados como fonte nesta avaliação.

## Orientações

- Justifique as respostas: identificar o resultado sem explicar o caminho não demonstra todo o raciocínio.
- Nas estruturas encadeadas, manipule os atributos dos nós; não substitua a estrutura por uma lista Python.
- No vetor estático, não utilize `append`, `insert`, `remove`, `pop` ou `index` para implementar as operações.
- Considere listas sem ciclos, exceto quando o enunciado disser que são circulares.
- As implementações das questões são independentes. Métodos com `self` devem ficar dentro da classe indicada.
- Para complexidade, considere comparação de valores e acesso a atributos com custo constante. N representa a quantidade de elementos.

Cada questão traz o gabarito logo abaixo. Para simular uma prova, tente resolver o enunciado antes de ler a resposta.

---

## Questão 1 — Abstração, TAD e memória (1,0 ponto)

Uma empresa precisa controlar vagões de um trem. Cada vagão possui nome, peso e uma referência para o próximo. A equipe considera representar a composição com um vetor de capacidade fixa ou com nós encadeados.

**a)** Explique o que significa abstrair esse problema e diferencie o “que faz” do “como faz”. **(0,3)**  
**b)** Diferencie capacidade de quantidade e explique subdimensionamento e superdimensionamento. **(0,3)**  
**c)** Como nós espalhados pela memória mantêm uma sequência? Qual o custo adicional dessa representação? **(0,2)**  
**d)** Diferencie dado e informação usando esse cenário. **(0,2)**

### Gabarito comentado

**a)** Abstrair é selecionar características relevantes para o objetivo. Para calcular o peso e reorganizar o trem, modelamos nome, peso e próximo vagão, sem precisar representar todos os detalhes físicos de um trem. O **que** corresponde às operações e ao comportamento esperado: inserir, remover, consultar e calcular o peso. O **como** corresponde à implementação: posições de vetor ou ligações entre nós. Um TAD descreve operações e regras sem obrigar uma implementação específica.

**b)** Capacidade é o máximo que cabe; quantidade é o total armazenado agora. Um vetor com capacidade 10 e três vagões possui sete posições livres. Reservar menos espaço que o necessário causa subdimensionamento; reservar muito mais do que se usa causa superdimensionamento. No modelo fixo, uma inserção deve ser recusada quando a quantidade atinge a capacidade.

**c)** Cada nó guarda uma referência para o próximo; a ordem lógica depende dessas ligações, e não da proximidade física dos objetos. O custo extra inclui as referências e a sobrecarga dos objetos e do gerenciamento de memória. Uma lista dupla guarda duas referências por nó.

**d)** `80.0` é um dado numérico. “A locomotiva pesa 80 toneladas” dá contexto ao dado. “A composição pesa 170 toneladas”, obtido somando os pesos, é uma informação produzida pelo processamento.

**Atenção para Python:** usar `[None] * 10` e impedir mudanças no tamanho físico simula um vetor de capacidade fixa. A lista Python em si continua sendo um objeto criado dinamicamente.

---

## Questão 2 — Complexidade e comparação de estruturas (1,0 ponto)

**a)** Ordene as taxas de crescimento da menor para a maior: O(N²), O(1), O(N), O(log N). **(0,2)**  
**b)** Informe a complexidade de pior caso das operações da tabela. **(0,6)**  
**c)** Explique por que inserir no início de um vetor tem custo diferente de inserir na cabeça de uma lista encadeada. **(0,2)**

### Gabarito comentado

**a)** **O(1) → O(log N) → O(N) → O(N²)**. A ordem representa crescimento assintótico; não é uma medição exata em segundos.

**b)**

| Operação | Custo | Justificativa |
| --- | --- | --- |
| Acessar posição válida de vetor pelo índice | O(1) | Acesso direto à posição. |
| Buscar valor em vetor não ordenado | O(N) | Pode ser necessário examinar todos os elementos. |
| Inserir no início de vetor com espaço disponível | O(N) | Desloca os elementos existentes. |
| Inserir no fim de vetor com espaço disponível | O(1) | Escreve na próxima posição livre. |
| Inserir no fim de lista simples que guarda apenas cabeça | O(N) | Precisa localizar o último nó. |
| Inserir no fim de lista dupla que guarda cauda | O(1) | A cauda já está disponível. |
| Remover por valor em lista simples | O(N) | Primeiro precisa localizar o alvo e seu antecessor. |
| Avançar uma faixa em player circular | O(1) | Segue uma referência. |

**c)** No vetor, abrir espaço no início exige mover os N elementos. Na lista encadeada, basta fazer o novo nó apontar para a cabeça antiga e atualizar a cabeça. O número de ajustes não depende de N.

**Erro comum:** dizer que toda remoção em lista encadeada é O(1). O ajuste pode ser O(1), mas buscar o elemento pelo valor custa O(N) no pior caso.

---

## Questão 3 — Vetor estático e remoção por deslocamento (1,0 ponto)

Considere a estrutura:

```python
class VetorEstatico:
    def __init__(self, capacidade=6):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.tamanho = 0
```

**a)** Implemente `inserir(valor)`, retornando `False` se o vetor estiver cheio. **(0,3)**  
**b)** Implemente `remover_impares()`. Cada remoção deve deslocar os elementos à direita uma posição para a esquerda. **(0,5)**  
**c)** Mostre o vetor físico e o tamanho lógico após inserir `7, 9, 12, 15, 18, 3` e remover os ímpares. **(0,2)**

### Gabarito comentado

Os métodos abaixo pertencem a `VetorEstatico`:

```python
def inserir(self, valor):
    if self.tamanho == self.capacidade:
        return False  # Não existe posição livre.
    self.dados[self.tamanho] = valor  # Escreve antes de incrementar.
    self.tamanho += 1
    return True

def remover_impares(self):
    indice = 0
    while indice < self.tamanho:
        if self.dados[indice] % 2 != 0:
            for j in range(indice, self.tamanho - 1):
                self.dados[j] = self.dados[j + 1]
            self.tamanho -= 1
            self.dados[self.tamanho] = None
            # Não avança: o valor que veio da direita ainda será analisado.
        else:
            indice += 1
```

**Simulação da parte ocupada:**

```text
Inicial:     [7, 9, 12, 15, 18, 3]
Remove 7:    [9, 12, 15, 18, 3]
Remove 9:    [12, 15, 18, 3]
Mantém 12.
Remove 15:   [12, 18, 3]
Mantém 18.
Remove 3:    [12, 18]
```

**Resposta c:** vetor físico `[12, 18, None, None, None, None]`; tamanho lógico `2`; capacidade `6`.

**Por que não incrementar sempre?** Ao remover 7, o 9 ocupa o índice 0. Se o índice avançasse imediatamente para 1, o 9 seria ignorado.

**Custo:** inserção O(1); remoção de todos os ímpares por deslocamentos O(N²) no pior caso.

---

## Questão 4 — Trem: inserir e desengatar vagões (1,0 ponto)

Considere um `Node` com `nome`, `peso` e `proximo`. A composição inicial é:

```text
Locomotiva (80) -> Carga (50) -> Passageiros (30) -> Cauda (10) -> None
```

**a)** Supondo que `carga` referencia o nó Carga, insira Restaurante, de 25 toneladas, entre Carga e Passageiros. Não recrie os nós existentes. **(0,2)**  
**b)** Implemente `desengatar_vagao(primeiro_no, nome_alvo)`, incluindo remoção da cabeça, alvo inexistente e desligamento do nó retirado. **(0,6)**  
**c)** Após inserir Restaurante e remover Carga, informe a ordem, a quantidade de nós e o peso total. **(0,2)**

### Gabarito comentado

```python
class Node:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = float(peso)
        self.proximo = None

# a) Primeiro preserva o acesso ao sucessor; depois altera a ligação de Carga.
restaurante = Node("Restaurante", 25.0)
restaurante.proximo = carga.proximo
carga.proximo = restaurante
```

```python
def desengatar_vagao(primeiro_no, nome_alvo):
    anterior = None
    atual = primeiro_no
    while atual is not None:
        if atual.nome == nome_alvo:
            if anterior is None:
                primeiro_no = atual.proximo  # Troca a cabeça.
            else:
                anterior.proximo = atual.proximo  # Pula o nó alvo.
            atual.proximo = None  # Isola após aproveitar seu sucessor.
            return primeiro_no
        anterior = atual
        atual = atual.proximo
    return primeiro_no  # Não encontrou: mantém a cabeça original.
```

A chamada deve guardar o retorno:

```python
primeiro = desengatar_vagao(primeiro, "Carga")
```

**Resposta c:** `Locomotiva → Restaurante → Passageiros → Cauda → None`; **4 nós**, incluindo a locomotiva; **145 toneladas**.

**Por que retornar a cabeça?** Se o alvo for o primeiro nó, o chamador precisa receber o novo ponto de entrada. Mudar apenas o parâmetro local não reatribui a variável `primeiro` do chamador.

---

## Questão 5 — Inversão de lista simples e interpretação de referências (1,0 ponto)

**a)** Implemente `inverter(primeiro_no)`, retornando a nova cabeça, sem criar nós ou listas auxiliares. **(0,5)**  
**b)** Simule as referências `anterior` e `atual` ao inverter `10 → 20 → 30 → None`. **(0,3)**  
**c)** Explique a diferença entre `atual = atual.proximo` e `atual.proximo = anterior`. **(0,2)**

### Gabarito comentado

```python
def inverter(primeiro_no):
    anterior = None
    atual = primeiro_no
    while atual is not None:
        proximo = atual.proximo  # Salva o caminho original.
        atual.proximo = anterior  # Vira a ligação para trás.
        anterior = atual  # Amplia a parte já invertida.
        atual = proximo  # Continua pela parte ainda não processada.
    return anterior
```

| Momento | Parte invertida, iniciada em anterior | atual |
| --- | --- | --- |
| Inicial | Vazia | Nó 10 |
| Após a primeira passagem | 10 → None | Nó 20 |
| Após a segunda passagem | 20 → 10 → None | Nó 30 |
| Após a terceira passagem | 30 → 20 → 10 → None | None |

**Resposta c:** `atual = atual.proximo` muda o objeto referenciado pela variável local `atual`. Já `atual.proximo = anterior` modifica um atributo do nó, alterando a estrutura da corrente.

**Por que salvar `proximo`?** Depois de virar a ligação, `atual.proximo` já não indica o sucessor original. Sem salvá-lo, perderíamos o caminho necessário para continuar a inversão.

**Casos limites:** vazia retorna `None`; unitária retorna o mesmo nó. **Complexidade:** O(N) em tempo e O(1) em espaço auxiliar.

---

## Questão 6 — Lista dupla: inserção e divisão em metades (1,0 ponto)

Considere `NodeDuplo`, com `dado`, `anterior` e `proximo`, e `ListaDupla`, com `cabeca`, `cauda` e `tamanho`. Uma nova lista começa com ambas as pontas em `None` e tamanho zero.

**a)** Implemente `inserir_fim(valor)`. **(0,3)**  
**b)** Implemente `split_metade()`, reaproveitando os nós e retornando dois gerenciadores independentes. Para tamanho ímpar, a segunda metade recebe o elemento extra. A lista de origem deve ficar vazia após a transferência. **(0,5)**  
**c)** Mostre o resultado para `50 ↔ 30 ↔ 22 ↔ 18 ↔ 12`. **(0,2)**

### Gabarito comentado

Métodos de `ListaDupla`:

```python
def inserir_fim(self, valor):
    novo = NodeDuplo(valor)
    novo.anterior = self.cauda
    if self.cabeca is None:
        self.cabeca = novo
    else:
        self.cauda.proximo = novo
    self.cauda = novo
    self.tamanho += 1

def split_metade(self):
    primeira = ListaDupla()
    segunda = ListaDupla()
    corte = self.tamanho // 2
    primeira.tamanho = corte
    segunda.tamanho = self.tamanho - corte

    if corte == 0:  # Origem vazia ou com um único nó.
        segunda.cabeca = self.cabeca
        segunda.cauda = self.cauda
    else:
        fim = self.cabeca
        for _ in range(corte - 1):
            fim = fim.proximo
        primeira.cabeca = self.cabeca
        primeira.cauda = fim
        segunda.cabeca = fim.proximo  # Salva antes de cortar.
        segunda.cauda = self.cauda
        primeira.cauda.proximo = None
        segunda.cabeca.anterior = None

    self.cabeca = None  # Os nós passam a pertencer às novas listas.
    self.cauda = None
    self.tamanho = 0
    return primeira, segunda
```

**Resposta c:**

```text
Primeira: None <- 50 <-> 30 -> None       tamanho = 2
Segunda:  None <- 22 <-> 18 <-> 12 -> None tamanho = 3
Origem:   vazia
```

**Por que cortar os dois sentidos?** Cortar somente `30.proximo` interrompe a leitura para frente, mas `22.anterior` ainda ligaria a segunda metade à primeira. As estruturas não estariam independentes.

**Custos:** inserir no fim O(1); localizar o ponto de divisão O(N). A divisão cria dois gerenciadores, mas não duplica os nós.

---

## Questão 7 — Player circular: navegação, remoção e condição de parada (1,0 ponto)

Um player circular duplo possui as faixas `A ↔ B ↔ C`, com a cauda C ligada à cabeça A. A faixa atual começa em A.

**a)** Qual é a faixa atual após quatro avanços e dois retornos? **(0,2)**  
**b)** Escreva uma função que exiba os títulos em exatamente uma volta. **(0,3)**  
**c)** Escreva os ajustes necessários para remover um nó `alvo` já localizado. Trate o caso unitário e a remoção da faixa atual, adotando o sucessor como nova faixa atual. **(0,5)**

### Gabarito comentado

**a)** Avanços: `A → B → C → A → B`. Retornos: `B → A → C`. **Resultado: C**.

```python
def exibir_uma_volta(cabeca):
    if cabeca is None:
        print("Playlist vazia")
        return
    atual = cabeca
    while True:
        print(atual.titulo)
        atual = atual.proximo
        if atual is cabeca:
            break  # Voltou ao MESMO objeto inicial.
```

Método do player, supondo `alvo` pertencente à estrutura:

```python
def remover_no(self, alvo):
    if alvo.proximo is alvo:  # Só existe esse nó.
        self.cabeca = None
        self.cauda = None
        self.faixa_atual = None
    else:
        alvo.anterior.proximo = alvo.proximo
        alvo.proximo.anterior = alvo.anterior
        if alvo is self.cabeca:
            self.cabeca = alvo.proximo
        if alvo is self.cauda:
            self.cauda = alvo.anterior
        if alvo is self.faixa_atual:
            self.faixa_atual = alvo.proximo
    alvo.proximo = None
    alvo.anterior = None
```

**Justificativa:** o vizinho da esquerda e o da direita passam a apontar um para o outro, preservando o anel. Só depois limpamos as ligações do retirado. Na lista unitária, não há outro nó que possa assumir suas funções.

**Erro comum:** usar `while atual is not None` em uma lista circular não vazia. Como a cauda volta à cabeça, essa condição nunca fica falsa.

**Custos:** navegação O(1); remoção de nó já localizado O(1); buscar pelo título para depois remover O(N).

---

## Questão 8 — Pipeline e eliminação circular (1,0 ponto)

A entrada do processo é `[12, 7, 18, 9, 22, 15, 30, 41, 50, 3]`.

**a)** Mostre a sequência após remover os ímpares, inverter a lista simples e dividir a lista dupla em duas metades. **(0,4)**  
**b)** Feche a segunda metade em um anel. Elimine de dois em dois, contando o nó atual como 1 e recomeçando no sucessor do retirado. Mostre os eliminados e o sobrevivente. **(0,3)**  
**c)** Escreva o método de eliminação para uma lista circular dupla com cabeça, cauda e tamanho, considerando `passos` um inteiro positivo. **(0,3)**

### Gabarito comentado

**a)**

```text
Após filtro:      12, 18, 22, 30, 50
Após inversão:   50 -> 30 -> 22 -> 18 -> 12 -> None
Primeira metade: 50 <-> 30
Segunda metade:  22 <-> 18 <-> 12
```

**b)**

| Rodada | Começa em | Contagem | Retirado | Próximo início |
| --- | --- | --- | --- | --- |
| 1 | 22 | 22 é 1; 18 é 2 | 18 | 12 |
| 2 | 12 | 12 é 1; 22 é 2 | 22 | 12 |

**Sobrevivente: 12.** Contar o atual como 1 implica avançar `passos - 1` referências, não `passos`. Essa é a regra detalhada do exercício, embora um trecho do enunciado original cite outro sobrevivente.

```python
def girar_e_eliminar(self, passos):
    if passos < 1:
        raise ValueError("Passos deve ser positivo.")
    if self.cabeca is None:
        raise ValueError("Lista vazia não tem sobrevivente.")
    atual = self.cabeca
    while self.tamanho > 1:
        for _ in range(passos - 1):
            atual = atual.proximo
        seguinte = atual.proximo
        atual.anterior.proximo = seguinte
        seguinte.anterior = atual.anterior
        if atual is self.cabeca:
            self.cabeca = seguinte
        if atual is self.cauda:
            self.cauda = atual.anterior
        atual.proximo = None
        atual.anterior = None
        self.tamanho -= 1
        atual = seguinte
    return self.cabeca.dado
```

O sobrevivente permanece em um anel de um nó: seu próximo e seu anterior apontam para ele mesmo. Para passo fixo 2, a eliminação é O(N); com passo variável P, esta implementação é O(N × P).

---

## Questão 9 — Pilha e fila de processos (1,0 ponto)

Uma pilha e uma fila recebem, nessa ordem, os valores `10, 20, 30`. Em seguida, cada estrutura remove um elemento, recebe `40` e consulta o próximo elemento a sair.

**a)** Informe os valores removidos, os valores consultados e a ordem final de saída das duas estruturas. **(0,3)**  
**b)** Implemente `push` e `pop` de uma pilha encadeada com `_topo` e `_tamanho`. **(0,3)**  
**c)** Implemente `enqueue` e `dequeue` de uma fila encadeada com `_frente`, `_fundo` e `_tamanho`. **(0,4)**

Considere `Node(valor)` com atributos `dado` e `proximo`, inicialmente `None`. Remover de estrutura vazia deve lançar `IndexError`.

### Gabarito comentado

| Estrutura | Primeiro removido | Consulta após inserir 40 | Ordem de saída restante |
| --- | --- | --- | --- |
| Pilha — LIFO | 30 | 40 | 40, 20, 10 |
| Fila — FIFO | 10 | 20 | 20, 30, 40 |

Métodos da pilha:

```python
def push(self, valor):
    novo = Node(valor)
    novo.proximo = self._topo
    self._topo = novo
    self._tamanho += 1

def pop(self):
    if self._topo is None:
        raise IndexError("Pilha vazia")
    removido = self._topo
    self._topo = removido.proximo
    removido.proximo = None
    self._tamanho -= 1
    return removido.dado
```

Métodos da fila:

```python
def enqueue(self, valor):
    novo = Node(valor)
    if self._frente is None:
        self._frente = novo
    else:
        self._fundo.proximo = novo
    self._fundo = novo
    self._tamanho += 1

def dequeue(self):
    if self._frente is None:
        raise IndexError("Fila vazia")
    removido = self._frente
    self._frente = removido.proximo
    if self._frente is None:
        self._fundo = None  # Saiu o último: não pode sobrar uma cauda antiga.
    removido.proximo = None
    self._tamanho -= 1
    return removido.dado
```

**Por que são O(1)?** As operações usam diretamente as pontas guardadas pela estrutura, sem percorrer os nós. Consultar (`peek` ou `front`) apenas lê o dado da ponta; não muda ligações nem tamanho.

---

## Questão 10 — Balanceamento de delimitadores e diagnóstico de erros (1,0 ponto)

**a)** Usando a classe `Pilha`, implemente `verificar_delimitadores(expressao)` para `()`, `[]` e `{}`. Ignore os demais caracteres. **(0,6)**  
**b)** Informe os resultados para as expressões da tabela e justifique as inválidas. **(0,2)**  
**c)** Por que contar apenas a quantidade de aberturas e fechamentos não resolve o problema? Qual o custo do algoritmo? **(0,2)**

### Gabarito comentado

Considere `Pilha` com os métodos `push`, `pop` e `esta_vazia` implementados na aula.

```python
def verificar_delimitadores(expressao):
    pilha = Pilha()
    for caractere in expressao:
        if caractere in "([{":
            pilha.push(caractere)
        elif caractere in ")]}":
            if pilha.esta_vazia():
                return False  # Fechamento sem abertura disponível.
            abertura = pilha.pop()
            if (
                (caractere == ")" and abertura != "(")
                or (caractere == "]" and abertura != "[")
                or (caractere == "}" and abertura != "{")
            ):
                return False  # A abertura mais recente era de outro tipo.
    return pilha.esta_vazia()  # Nenhuma abertura pode ficar pendente.
```

| Expressão | Resultado | Motivo |
| --- | --- | --- |
| `([]){}` | True | Todos os pares fecham na ordem correta. |
| `([)]` | False | Ao ler `)`, a abertura mais recente é `[`. |
| `(()` | False | Sobra uma abertura `(` na pilha. |
| `]` | False | Não existe abertura para o fechamento. |
| `a * (b + c[2])` | True | Os pares de delimitadores estão bem aninhados. |
| String vazia | True | Não há delimitador pendente. |

**Resposta c:** as contagens não registram a ordem. `([)]` tem um par de cada tipo, mas eles se cruzam. A pilha resolve porque o último delimitador aberto precisa ser o primeiro fechado. Para N caracteres, o algoritmo custa O(N) em tempo e O(N) de memória no pior caso, quando se acumulam N aberturas.

**Limite do exercício:** este algoritmo verifica caracteres; não interpreta strings, comentários ou todas as regras de uma linguagem de programação.

---

## Critérios de correção e revisão final

Nas questões práticas, a pontuação deve considerar tanto o caso normal quanto os casos explicitamente pedidos: estrutura vazia, unitária, remoção da cabeça e preservação das ligações. Soluções equivalentes são válidas se respeitarem as restrições.

Antes de encerrar uma resposta prática, confira:

1. **Entrada vazia:** a função evita acessar atributos de `None`?
2. **Um único elemento:** cabeça, cauda e contadores ficam corretos?
3. **Referências:** o sucessor foi salvo antes de sobrescrever uma ligação?
4. **Retorno:** o chamador recebe e guarda a nova cabeça quando necessário?
5. **Lista dupla:** os dois sentidos foram atualizados?
6. **Lista circular:** existe uma condição de parada que não dependa de `None`?
7. **Vetor:** quantidade e capacidade foram diferenciadas?
8. **Complexidade:** a busca foi incluída no custo, além do ajuste de referências?

**Distribuição:** conceitos e complexidade, 2,0 pontos; vetor e listas, 6,0 pontos; pilhas, filas e delimitadores, 2,0 pontos. **Total: 10,0 pontos.**
