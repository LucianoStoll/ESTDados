# =====================================================================
# 3. TESTES DE VERIFICAÇÃO
# =====================================================================
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