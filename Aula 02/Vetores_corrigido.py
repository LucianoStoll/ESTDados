# GUIA DE CONSULTA: LISTA SEQUENCIAL ESTÁTICA
# Sequencial: os elementos válidos ficam em posições consecutivas, sem buracos.
# Estática: a capacidade é definida no início e não cresce nas operações.
# Python possui listas dinâmicas; aqui simulamos uma estrutura estática usando
# uma lista de tamanho fixo, sem append, remove, index ou bibliotecas.
#
# ÍNDICE x VALOR: em [10, 20, 30], o valor 20 está no índice 1.
# Os índices começam em 0. Com 3 elementos, os índices válidos são 0, 1 e 2.
#
# CAPACIDADE x QUANTIDADE:
# Capacidade = número máximo de elementos que cabem na estrutura.
# Quantidade = número de elementos armazenados neste momento.
# Regra que todas as operações preservam: 0 <= quantidade <= CAPACIDADE.
# Posições ocupadas: de 0 até quantidade - 1.
# Próxima posição livre: quantidade (somente quando a lista não está cheia).

# Letras maiúsculas indicam, por convenção, um valor que não deve ser alterado.
CAPACIDADE = 5
# Cria 5 posições: [None, None, None, None, None]. None significa ausência
# de valor neste exemplo. A ocupação é controlada por quantidade, não por None.
Vet = [None] * CAPACIDADE
# A estrutura começa vazia, embora já tenha espaço reservado para 5 elementos.
quantidade = 0


def buscar_por_indice(indice):
    # Recebe uma posição inteira e devolve o valor guardado nessa posição.
    # "or" significa OU: basta uma das duas condições ser verdadeira.
    # Proibimos negativos (Python permitiria -1) e posições não ocupadas.
    # Com quantidade = 3, índice 3 já é inválido: o último válido é 2.
    if indice < 0 or indice >= quantidade:
        # raise sinaliza um erro e interrompe esta chamada da função.
        # Usamos erro em vez de None, pois None poderia ser um valor armazenado.
        raise IndexError("Índice fora das posições ocupadas.")
    # Os colchetes acessam diretamente a posição. return devolve o resultado
    # para quem chamou a função e encerra sua execução.
    return Vet[indice]


def buscar_por_valor(valor):
    # Busca sequencial: verifica os elementos um a um.
    # range(quantidade) gera 0 até quantidade - 1; o limite final é excluído.
    # Assim, não procuramos nas posições livres. Se estiver vazia, não há laço.
    for indice in range(quantidade):
        # == compara valores; = atribui um valor a uma variável.
        if Vet[indice] == valor:
            # Encerra na primeira ocorrência, mesmo que existam valores iguais.
            return indice
    # Só chega aqui se percorreu todos os elementos sem encontrar o valor.
    # -1 é nosso sinal de "não encontrado", pois índices válidos são >= 0.
    # Atenção: não use esse -1 para acessar Vet; em Python seria a última posição!
    return -1


def inserir(valor):
    # Esta versão insere no final da parte ocupada.
    # global permite reatribuir a variável quantidade definida fora da função.
    # Sem global, quantidade += 1 seria tratada como atribuição local e falharia.
    # Não precisamos de global Vet: alteramos um item, sem reatribuir Vet.
    global quantidade
    # Verifica a lotação ANTES de acessar a próxima posição livre.
    # Se quantidade == 5, Vet[5] não existe: os índices vão de 0 a 4.
    if quantidade == CAPACIDADE:
        # False indica falha. O retorno imediato impede alterar a lista cheia.
        return False
    # Exemplo: com 2 elementos, Vet[0] e Vet[1] estão ocupados;
    # o novo elemento deve entrar em Vet[2], isto é, Vet[quantidade].
    Vet[quantidade] = valor
    # Equivale a quantidade = quantidade + 1.
    # Incrementamos DEPOIS de inserir para não pular uma posição.
    quantidade += 1
    # True informa que a inserção foi realizada.
    return True


def remover(valor):
    # Remove por VALOR, não por índice, e apenas a primeira ocorrência.
    # Precisamos de global porque vamos diminuir a quantidade armazenada.
    global quantidade
    # Reutilizamos a busca para descobrir a posição do elemento a remover.
    indice = buscar_por_valor(valor)
    # Se não existe, não há nada para remover (inclui o caso de lista vazia).
    if indice == -1:
        return False
    # Para não deixar buraco, copiamos cada elemento seguinte uma posição
    # para a esquerda. Percorremos da posição removida até quantidade - 2.
    # O limite do range é excluído; assim posicao + 1 chega, no máximo,
    # a quantidade - 1, que era a última posição ocupada.
    # Exemplo: [10, 20, 30, 40, 50], removendo 30 (índice 2):
    # Vet[2] = Vet[3] -> [10, 20, 40, 40, 50]
    # Vet[3] = Vet[4] -> [10, 20, 40, 50, 50]
    # Se remover o último elemento, o range fica vazio: nada precisa deslocar.
    for posicao in range(indice, quantidade - 1):
        Vet[posicao] = Vet[posicao + 1]
    # Um elemento saiu; reduzimos o tamanho lógico da lista.
    quantidade -= 1
    # Após reduzir, quantidade aponta para a antiga última posição ocupada.
    # Limpamos a cópia restante: [10, 20, 40, 50, None].
    # A capacidade continua sendo 5; agora só 4 posições estão ocupadas.
    Vet[quantidade] = None
    # Informa que o valor foi encontrado e removido.
    return True


def exibir():
    # Função auxiliar: mostra os elementos válidos, sem as posições livres.
    # end="" evita a quebra de linha automática do print.
    print("[", end="")
    # Percorre somente a parte ocupada. Se vazia, imprime apenas [].
    for indice in range(quantidade):
        # Coloca separador antes de cada elemento, exceto o primeiro.
        # Isso evita vírgula sobrando no começo ou no final da lista.
        if indice > 0:
            print(", ", end="")
        # Mostra o elemento na mesma linha que os anteriores.
        print(Vet[indice], end="")
    # Fecha a representação e, sem end="", termina com uma quebra de linha.
    print("]")


# Quando executamos este arquivo diretamente, __name__ vale "__main__".
# Esse teste faz o exemplo rodar só nessa situação. Se outro arquivo importar
# as funções, o exemplo não executará nem preencherá a lista automaticamente.
if __name__ == "__main__":
    inserir(10)  # Guarda no índice 0; quantidade passa a 1.
    inserir(20)  # Guarda no índice 1; quantidade passa a 2.
    inserir(30)  # Guarda no índice 2; quantidade passa a 3.
    inserir(40)  # Guarda no índice 3; quantidade passa a 4.
    inserir(50)  # Guarda no índice 4; quantidade passa a 5 (cheia).

    exibir()  # Mostra [10, 20, 30, 40, 50].
    print(buscar_por_indice(2))  # Procura pela posição 2: devolve o valor 30.
    print(buscar_por_valor(10))  # Procura pelo valor 10: devolve o índice 0.
    # inserir é executada e seu retorno é impresso: False, pois não há espaço.
    print("Inserção com lista cheia:", inserir(60))

    remover(30)  # Desloca 40 e 50 à esquerda; quantidade passa a 4.
    exibir()  # Mostra [10, 20, 40, 50].

    inserir(60)  # Usa Vet[4], que ficou livre; quantidade volta a 5.
    exibir()  # Mostra [10, 20, 40, 50, 60].


# RESUMO PARA A PROVA
# buscar_por_indice: recebe índice; retorna valor; índice inválido gera erro.
# buscar_por_valor: recebe valor; retorna primeiro índice encontrado ou -1.
# inserir: recebe valor; retorna True se inseriu ou False se cheia.
# remover: recebe valor; retorna True se removeu ou False se não encontrou.
# exibir: imprime os elementos; não tem retorno explícito (retorna None).
#
# CUSTO DAS OPERAÇÕES (n = quantidade de elementos; comparação de custo constante):
# Busca por índice: O(1), pois acessa diretamente uma posição.
# Busca por valor: O(n) no pior caso, pois pode verificar todos os elementos.
# Inserção no final: O(1), pois não desloca elementos nem aumenta a capacidade.
# Remoção por valor: O(n) no pior caso, pela busca e pelos deslocamentos.
# Exibição: O(n), pois visita todos os elementos válidos.
# O(1) = trabalho constante; O(n) = trabalho que cresce linearmente com n.
#
# ERROS COMUNS:
# - Confundir capacidade com quantidade e acessar posições ainda livres.
# - Esquecer que range não inclui seu limite final.
# - Aumentar quantidade antes de guardar o novo elemento.
# - Remover sem deslocar os seguintes, deixando um buraco na parte ocupada.
# - Usar o -1 da busca como índice sem verificar se o valor foi encontrado.
