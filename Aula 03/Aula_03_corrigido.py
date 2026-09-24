# AULA 03 — TREM DE CARGA: LISTA SIMPLESMENTE ENCADEADA
# Objetivo: representar vagões como objetos ligados por referências.
# Cada nó guarda dados (nome e peso) e uma referência para o próximo nó.
# Não usamos list, tuple, dict ou set para armazenar a sequência.
#
# REFERÊNCIA: uma variável como no1 permite acessar um objeto Node.
# Atribuir atual = primeiro_no NÃO copia o nó: ambas apontam para o mesmo objeto.
# Alterar atual.proximo muda esse objeto; fazer atual = atual.proximo apenas
# muda qual objeto a variável atual referencia.
#
# CABEÇA: referência para o primeiro nó. É a entrada para percorrer a corrente.
# CAUDA: último nó, cujo proximo é None (não há sucessor).
# A lista vazia é representada por uma cabeça igual a None.
# Diferentemente de um vetor, não acessamos o terceiro nó por índice direto:
# precisamos seguir as referências desde a cabeça.


class Node:
    # A classe é o modelo; cada chamada Node(...) cria um objeto independente.
    # __init__ inicializa os atributos do novo objeto.
    # self representa a instância que está sendo inicializada.
    def __init__(self, nome, peso):
        self.nome = nome  # Identificador textual do vagão.
        self.peso = float(peso)  # Guarda o peso em toneladas como float.
        # O novo nó começa desengatado. Ligamos os nós depois da criação.
        # Não precisamos receber proximo como argumento se ele começa em None.
        self.proximo = None


# As operações abaixo são funções fora da classe: recebem a cabeça do trem.
# A classe representa um vagão; essas funções trabalham sobre a corrente.
def relatorio_trem(primeiro_no):
    # Usamos uma referência auxiliar para percorrer sem perder a cabeça.
    atual = primeiro_no
    peso_total = 0.0  # Acumulador: começa em zero e recebe cada peso visitado.
    quantidade = 0  # Contador: aumenta uma vez para cada nó visitado.

    # Continua enquanto houver um nó. "is not None" testa se a referência
    # não é None. Nunca acessamos atual.nome quando atual é None.
    while atual is not None:
        peso_total += atual.peso  # Equivale a peso_total = peso_total + atual.peso.
        quantidade += 1  # Inclui a locomotiva, pois ela também é um nó do trem.
        # f permite inserir expressões entre chaves; :.1f mostra uma decimal.
        # end="" evita quebrar a linha, formando um desenho contínuo do trem.
        print(f"[ {atual.nome} ({atual.peso:.1f}t) ] -> ", end="")
        # Avança para o próximo nó. Sem este passo, o laço nunca terminaria
        # em uma corrente não vazia, pois atual continuaria no mesmo nó.
        atual = atual.proximo

    # Só depois do laço atual é None: aqui chegamos ao fim da corrente.
    # Um teste atual is None dentro desse while, antes de avançar, seria falso.
    print("FIM")
    print(f"Quantidade de vagões (incluindo a locomotiva): {quantidade}")
    print(f"Peso total do trem: {peso_total:.1f} t")
    # Não há return explícito: a função imprime o relatório e retorna None.
    # Por isso chamamos relatorio_trem(...) sem envolvê-la em print(...).


def desengatar_vagao(primeiro_no, nome_alvo):
    # atual procura o alvo; anterior acompanha o nó imediatamente anterior.
    atual = primeiro_no
    anterior = None  # A cabeça não tem antecessor.

    while atual is not None:
        # == compara o conteúdo do nome. Se houver nomes repetidos,
        # esta função remove apenas a primeira ocorrência.
        if atual.nome == nome_alvo:
            if anterior is None:
                # O alvo é a cabeça: o sucessor passa a ser a nova cabeça.
                # Se for o único nó, atual.proximo é None e o trem fica vazio.
                primeiro_no = atual.proximo
            else:
                # O antecessor passa a apontar para o sucessor, pulando o alvo.
                # Exemplo: A -> B -> C vira A -> C ao remover B.
                # Também funciona na cauda: seu sucessor é None.
                anterior.proximo = atual.proximo

            # Desliga o nó retirado da corrente. Faça isso APÓS aproveitar
            # seu sucessor, senão a referência para o restante seria perdida.
            atual.proximo = None
            # Retorna a cabeça atualizada e encerra a busca.
            return primeiro_no

        # A ordem importa: primeiro guardamos o nó atual como antecessor,
        # depois avançamos. Assim as duas referências andam juntas.
        anterior = atual
        atual = atual.proximo

    # Se a lista estiver vazia ou o nome não existir, devolve a cabeça original.
    # Sem este return, Python retornaria None e o chamador poderia perder
    # a entrada da corrente ao atribuir o resultado a primeiro.
    return primeiro_no


def inverter_trem(primeiro_no):
    # Inverte apenas as ligações: não cria nós nem uma sequência auxiliar.
    anterior = None  # Cabeça da parte já invertida, inicialmente vazia.
    atual = primeiro_no  # Primeiro nó da parte que ainda falta processar.

    while atual is not None:
        # 1. Salva o sucessor ANTES de sobrescrever atual.proximo.
        # Esta variável guarda só uma referência, não uma cópia do nó.
        proximo = atual.proximo
        # 2. Vira a ligação para trás, em direção à parte já invertida.
        # Na primeira passagem, a cabeça original vira cauda e aponta para None.
        atual.proximo = anterior
        # 3. O nó processado passa a ser a cabeça da parte invertida.
        anterior = atual
        # 4. Continua pela ligação original que salvamos no passo 1.
        atual = proximo

    # Ao terminar, atual é None e anterior é a antiga cauda: a nova cabeça.
    # Lista vazia retorna None; lista com um nó retorna esse mesmo nó.
    return anterior


# O exemplo executa apenas quando rodamos este arquivo diretamente.
# Importar este arquivo permite usar as funções sem executar a demonstração.
if __name__ == "__main__":
    # ALOCAÇÃO DINÂMICA: cada chamada cria um nó quando necessário.
    # Não reservamos previamente uma capacidade fixa de vagões.
    no1 = Node("Locomotiva", 80.0)
    no2 = Node("Vagão Carga", 50.0)
    no3 = Node("Vagão Passageiros", 30.0)
    no4 = Node("Vagão Cauda", 10.0)

    # Encadeamento manual inicial: no1 -> no2 -> no3 -> no4 -> None.
    no1.proximo = no2
    no2.proximo = no3
    no3.proximo = no4
    # no4.proximo já é None, definido no construtor.
    primeiro = no1  # Guardamos a entrada da corrente.

    print("COMPOSIÇÃO INICIAL")
    relatorio_trem(primeiro)  # 4 nós; peso total: 170.0 t.

    # INSERÇÃO INTERMEDIÁRIA: entra entre Carga e Passageiros.
    restaurante = Node("Vagão Restaurante", 25.0)
    # Primeiro preserva o sucessor do nó Carga: Restaurante -> Passageiros.
    restaurante.proximo = no2.proximo
    # Depois engata Carga -> Restaurante. O restante da corrente é preservado.
    # Se invertêssemos estas duas instruções, poderíamos criar um ciclo:
    # restaurante.proximo acabaria apontando para o próprio restaurante.
    no2.proximo = restaurante

    print("\nAPÓS INSERIR RESTAURANTE")  # \n pula uma linha na saída.
    relatorio_trem(primeiro)  # 5 nós; peso total: 195.0 t.

    # Sempre recebemos a cabeça devolvida: a remoção também pode trocar
    # o primeiro nó. Aqui a cabeça continua sendo a locomotiva.
    primeiro = desengatar_vagao(primeiro, "Vagão Carga")
    print("\nAPÓS REMOVER CARGA")
    relatorio_trem(primeiro)  # 4 nós; peso total: 145.0 t.
    # no2 ainda referencia o vagão retirado, mas no2.proximo agora é None.
    # Desengatar não significa destruir o objeto: enquanto existir referência
    # para ele, o objeto continua acessível. Python gerencia sua memória.

    # A inversão muda a cabeça, por isso guardar o retorno é indispensável.
    primeiro = inverter_trem(primeiro)
    print("\nAPÓS INVERTER O TREM")
    # Cauda -> Passageiros -> Restaurante -> Locomotiva -> FIM.
    relatorio_trem(primeiro)  # Mesmos 4 nós e 145.0 t; só muda a ordem.


# RESUMO PARA CONSULTA
# Inserir após um nó conhecido:
#   novo.proximo = anterior.proximo
#   anterior.proximo = novo
# Remover um nó com antecessor conhecido:
#   anterior.proximo = alvo.proximo
#   alvo.proximo = None
# Remover a cabeça:
#   primeiro = alvo.proximo
#   alvo.proximo = None
# Inverter: salvar sucessor -> virar ligação -> atualizar anterior -> avançar.
#
# SIMULAÇÃO DA INVERSÃO: A -> B -> C -> None
# Passagem 1: A -> None; anterior é A; atual é B.
# Passagem 2: B -> A -> None; anterior é B; atual é C.
# Passagem 3: C -> B -> A -> None; anterior é C; atual é None.
# Retornamos C, a nova cabeça.
#
# CUSTOS (n = número de nós; considerando comparação de nomes constante):
# Relatório: O(n), pois visita todos os nós.
# Inserção após nó já conhecido: O(1), pois ajusta apenas duas referências.
# Remoção por nome: O(n) no pior caso para localizar o alvo;
# o ajuste das ligações, depois de encontrá-lo, é O(1).
# Inversão: O(n) em tempo e O(1) em espaço auxiliar: usa só algumas referências.
# A corrente inteira ocupa O(n) de memória: cada nó armazena dados e uma ligação.
#
# CUIDADOS PARA A PROVA
# - Salve o sucessor antes de sobrescrever uma ligação necessária.
# - Atualize a cabeça com o retorno da remoção e da inversão.
# - Não confunda mover uma variável com modificar o objeto referenciado.
# - Não esqueça de avançar no while e de tratar a lista vazia.
# - As funções pressupõem uma corrente sem ciclos, terminada em None.
# - Nenhuma função precisa de global: recebe a cabeça como parâmetro,
#   modifica os objetos e devolve uma nova cabeça quando necessário.
