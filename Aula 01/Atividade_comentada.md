# Aula 01 — Respostas explicadas para consulta

Este guia responde ao enunciado de `Atividade.txt` com os conceitos gerais de estruturas de dados. Não é uma transcrição nem uma conferência dos PDFs da aula.

## 1. Abstração e separação do que e do como

**(a)** Abstrair é selecionar as características relevantes para resolver um problema e deixar de lado detalhes que não interferem nessa solução. Em um sistema de trem, um nó pode guardar nome, peso e próximo vagão; não precisamos modelar a cor dos bancos para calcular o peso total.

**(b)** O **que** define as operações e seus resultados; o **como** define a implementação. Um TAD pilha oferece empilhar, desempilhar e consultar o topo, mantendo a regra de que o último a entrar sai primeiro. Ele pode ser implementado com vetor ou nós encadeados. Separar interface e implementação permite trocar a estrutura interna sem exigir que o restante do programa conheça suas ligações ou posições de memória.

## 2. Alocação estática e dinâmica

**(a)** No modelo didático de estrutura estática, reserva-se uma capacidade fixa que não cresce durante as operações. Se reservarmos 10 posições e precisarmos de 11, ocorre **subdimensionamento**: falta espaço. Se usarmos apenas 2, as demais ficam ociosas, caracterizando **superdimensionamento**. Capacidade é o limite; quantidade é o que está ocupado.

**(b)** Na alocação dinâmica, o programa solicita espaço conforme a necessidade durante a execução. Em uma lista encadeada, novos nós são criados à medida que inserimos elementos. Além dos dados, armazenamos referências para os vizinhos; também existe sobrecarga do gerenciamento de memória e dos objetos. A estrutura pode crescer, mas continua limitada pela memória disponível.

**Cuidado com Python:** `[None] * 10` cria uma lista Python durante a execução. Ela não é uma declaração de array estático como em C. Nos exercícios, simulamos capacidade fixa ao não aumentar nem diminuir o tamanho físico dessa lista. O termo “estático” aqui descreve essa regra da estrutura.

## 3. Dado, tipo de dado e informação

**(a)** Dado é uma representação de um valor, como `30`, `"Ana"` ou `True`. Um tipo de dado determina os valores e operações associados: números permitem operações aritméticas; textos têm operações próprias, como concatenação. O número `30` e o texto `"30"` não são a mesma coisa para o programa.

**(b)** Informação é o significado obtido ao contextualizar ou processar dados. `30` isoladamente é um dado; “o vagão pesa 30 toneladas” atribui contexto. Somar os pesos dos vagões produz a informação “peso total da composição”.

## 4. Estruturas sequenciais estáticas e dinâmicas

**(a)** Em um array contíguo tradicional, os elementos ocupam posições consecutivas de memória. Conhecendo o endereço inicial e o tamanho de cada elemento, calcula-se diretamente onde está o índice desejado: `base + indice * tamanho_do_elemento`. Por isso o acesso por índice é O(1).

**(b)** Em uma lista encadeada, a ordem é definida pelas referências. Um nó guarda o caminho para o próximo, mesmo que eles estejam em regiões diferentes da memória. Começamos na cabeça e seguimos `proximo` até `None`; em uma lista circular, paramos após uma volta. Para chegar ao elemento de posição k, normalmente precisamos percorrer os anteriores.

## Revisão rápida

| Conceito | Lembrete |
| --- | --- |
| TAD | Operações e comportamento, separados da implementação |
| Vetor de capacidade fixa | Índices diretos; pode exigir deslocamentos |
| Nó encadeado | Dados e referência para outro nó |
| Cabeça | Entrada da lista |
| Abstração | Modelar só o necessário para o problema |
