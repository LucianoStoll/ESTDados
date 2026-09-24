# Aula 03 — Complexidade das operações

Respostas conceituais ao `Atividade.txt`. O enunciado pede pesquisa bibliográfica; este guia explica o raciocínio, mas não substitui essa pesquisa nem atribui respostas a uma bibliografia que não foi consultada.

## 1. Ordem de crescimento

Da menor para a maior taxa de crescimento: **O(1) → O(log N) → O(N) → O(N²)**.

- **O(1):** quantidade de trabalho limitada por uma constante, independentemente de N. Exemplo: acessar um índice de vetor.
- **O(log N):** o problema diminui por um fator constante a cada etapa. Exemplo: busca binária em vetor ordenado.
- **O(N):** o trabalho cresce proporcionalmente ao número de elementos. Exemplo: busca linear no pior caso.
- **O(N²):** o trabalho pode crescer proporcionalmente ao quadrado da entrada. Exemplo: percorrer N elementos para cada um dos N elementos.

Big-O descreve um limite assintótico de crescimento, não um número exato de segundos. Essa ordem compara as taxas usuais; constantes e tamanho da entrada também influenciam o tempo real. Aqui usamos os limites usuais mais informativos para cada operação.

## 2. Operações em vetores — pior caso

| Item | Operação | Custo | Por quê |
| --- | --- | --- | --- |
| a | Acessar pelo índice | O(1) | A posição pode ser localizada diretamente. |
| b | Buscar valor sequencialmente | O(N) | O valor pode ser o último ou não existir; é preciso examinar todos. |
| c | Inserir no início | O(N) | Os N elementos existentes precisam ser deslocados para abrir espaço. |
| d | Inserir no fim com espaço disponível | O(1) | Escreve na próxima posição e atualiza o tamanho, sem deslocar. |

Exemplo: inserir 5 no início de `[10, 20, 30]` exige mover 30, depois 20, depois 10 para a direita e só então escrever 5. Mover da direita para a esquerda evita sobrescrever dados que ainda precisam ser copiados.

**Condição do item d:** o vetor precisa ter espaço livre. Em uma lista dinâmica, uma inserção que exige realocação pode custar O(N); não é o caso descrito nesse item.

**Não confunda com lista encadeada:** inserir na cabeça de uma lista encadeada custa O(1), pois basta ajustar referências. A mesma inserção no início de um vetor custa O(N), por causa dos deslocamentos.
