# DEMONSTRAÇÃO DA LISTA DUPLA LINEAR.
# O original usava a classe sem importá-la, causando NameError ao rodar sozinho.
# Este import busca o arquivo vizinho Definicao_corrigido.py e traz a classe.
from Definicao_corrigido import ListaDuplamenteEncadeada

# __name__ impede que a demonstração rode ao importar este módulo.
# Os testes abaixo mostram casos vazio, unitário e com vários elementos.
# inserir_inicio inverte a ordem das inserções; inserir_fim preserva essa ordem.
# Resultado final da leitura para frente:
# 5 <-> 10 <-> 15 <-> 25 <-> 50 <-> 75 <-> 90 <-> 100 <-> None.
# A leitura para trás deve mostrar exatamente o inverso.

if __name__ == "__main__":
    lista = ListaDuplamenteEncadeada()

    print("--- Teste 1: Estado Inicial da Lista ---")
    print("A lista está vazia?", lista.esta_vazia())
    lista.imprimir_frente()
    lista.imprimir_tras()

    print("\n--- Teste 2: Inserção do Primeiro Elemento (25) ---")
    lista.inserir_inicio(25)
    lista.imprimir_frente()
    lista.imprimir_tras()

    print("\n--- Teste 3: Inserções Sequenciais no Início (15, 10, 5) ---")
    lista.inserir_inicio(15)
    lista.inserir_inicio(10)
    lista.inserir_inicio(5)
    lista.imprimir_frente()
    lista.imprimir_tras()

    print("\n--- Teste 4: Inserções Sequenciais no Fim (50, 75, 90, 100) ---")
    lista.inserir_fim(50)
    lista.inserir_fim(75)
    lista.inserir_fim(90)
    lista.inserir_fim(100)
    lista.imprimir_frente()
    lista.imprimir_tras()

    print("\n--- Teste 5: Verificação de Estado Final ---")
    print("A lista está vazia?", lista.esta_vazia())