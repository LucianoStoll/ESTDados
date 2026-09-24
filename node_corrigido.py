# REFERÊNCIAS E NÓS — primeiro exemplo de lista encadeada.
# Um nó guarda um dado e a referência para o próximo nó.
# As referências estabelecem a ordem; os objetos não precisam estar juntos
# na memória. None representa a ausência de um próximo nó.

class Node:
    # self é o objeto que está sendo inicializado; dado é o valor recebido.
    def __init__(self, dado):
        self.dado = dado  # Atributo que armazena o conteúdo do nó.
        self.proximo = None  # Cada nó nasce desligado dos outros.


if __name__ == "__main__":  # Não executa a demonstração ao importar o arquivo.
    no1 = Node("A")  # Cada chamada cria um objeto diferente.
    no2 = Node("B")
    no3 = Node("C")
    no4 = Node("D")

    no1.proximo = no2  # A aponta para B; não estamos copiando B.
    no2.proximo = no3  # B aponta para C.
    no3.proximo = no4  # C aponta para D; D continua apontando para None.
    primeiro = no1  # Guarda a cabeça, a entrada para acessar toda a corrente.

    # Usamos atual para não terminar com primeiro = None, perdendo a cabeça.
    atual = primeiro
    while atual is not None:  # Só acessa atributos enquanto existir um nó.
        print(atual.dado)  # Saída: A, B, C e D, um por linha.
        atual = atual.proximo  # Avança; sem isso o laço não terminaria.

# RESUMO: atual = atual.proximo move a variável; atual.proximo = outro
# modifica a ligação do objeto. São operações diferentes!
# A varredura visita n nós: O(n) em tempo e O(1) em espaço auxiliar.
# Uma corrente vazia tem primeiro = None; o while não executa nenhuma vez.
