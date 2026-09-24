# Guia de consulta dos exercícios

Os arquivos originais foram preservados. Use as versões abaixo: elas incluem explicações de funcionamento, motivo das operações, custos e cuidados comuns. Os PDFs originais não foram alterados nem revisados neste trabalho.

| Assunto | Arquivo |
| --- | --- |
| Abstração, memória e TADs | [Aula 01 — atividade comentada](Aula%2001/Atividade_comentada.md) |
| Vetor de capacidade fixa | [Aula 02](Aula%2002/Vetores_corrigido.py) |
| Referências e nós básicos | [node corrigido](node_corrigido.py) |
| Trem e inversão de referências | [Aula 03](Aula%2003/Aula_03_corrigido.py) |
| Complexidade das operações | [Aula 03 — atividade comentada](Aula%2003/Atividade_comentada.md) |
| Lista simplesmente encadeada | [Aula 04](Aula%2004/Aula_04_corrigido.py) |
| Lista dupla linear | [Aula 05 — definição](Aula%2005/Definicao_corrigido.py) |
| Exemplos da lista dupla linear | [Aula 05 — testes](Aula%2005/Bloco_de_Testes_corrigido.py) |
| Player circular duplo | [Aula 05 — player](Aula%2005/ListaDuplamenteEncadeada_corrigido.py) |
| Conversões, divisão e eliminação circular | [Aula 06](Aula%2006/Pipeline_corrigido.py) |
| Pilha, fila e delimitadores | [Aula 07](Aula%2007/laboratorio_de_pilhas_e_filas_corrigido.py) |

## Como executar

Abra o arquivo desejado e execute com Python. Pelo terminal, a partir desta pasta, por exemplo: `python "Aula 06/Pipeline_corrigido.py"`.

Na Aula 05, execute `Bloco_de_Testes_corrigido.py` para demonstrar a lista dupla linear. Mantenha esse arquivo junto de `Definicao_corrigido.py`, que ele importa.

## Decisões importantes

- Aula 05: o arquivo de definição é uma lista dupla **linear**; o player é **circular**. Na linear, as pontas terminam em None. Na circular, elas se ligam.
- Aula 06: pela regra detalhada de contar o nó atual como 1, o sobrevivente do exemplo é **12**. O trecho do enunciado que menciona 22 contradiz essa regra e o teste final.
- Aula 06: dividir transfere os nós para as duas metades e esvazia a estrutura original; converter a metade em circular também esvazia o gerenciador de origem. Isso evita manter estruturas antigas com referências inconsistentes.
- As atividades teóricas receberam respostas explicadas com base nos enunciados TXT. Não são transcrições dos slides nem pesquisa bibliográfica.

## Comparação rápida

| Estrutura | Entrada e saída | Cuidado principal |
| --- | --- | --- |
| Vetor fixo | Posições por índice | Distinguir capacidade de quantidade |
| Lista simples | Referência para o próximo | Preservar o caminho antes de mudar ligações |
| Lista dupla | Anterior e próximo | Atualizar os dois sentidos |
| Lista circular | Último ligado ao primeiro | Parar após uma volta, não esperar None |
| Pilha | Entra e sai pelo topo: LIFO | Último inserido sai primeiro |
| Fila | Entra no fundo e sai na frente: FIFO | Ao esvaziar, limpar frente e fundo |
