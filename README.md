# Labirinto
Prova do Fabio 
Defina o Labirinto:

Represente o labirinto como uma matriz de quadrados, onde cada quadrado pode ser aberto ou ocupado por uma parede.
Use uma convenção, como 0 para quadrados abertos e 1 para paredes.
Encontre a Saída:

Comece na posição inicial (por exemplo, a entrada do labirinto).
Tente mover-se em uma direção (norte, sul, leste ou oeste).
Se a próxima posição estiver dentro dos limites do labirinto e for um quadrado aberto, mova-se para lá.
Se a próxima posição for uma parede ou estiver fora dos limites, tente outra direção.
Continue até encontrar a saída ou até não haver mais opções.
Backtracking:

Se você ficar preso (não houver mais opções), volte para a última posição onde havia escolhas.
Marque as posições visitadas para evitar loops infinitos.
Tente outras direções a partir dessa posição.
Recursão:

Use recursão para explorar todas as possibilidades.
Lembre-se de marcar as posições visitadas para evitar loops.
Usa as seguintes Buscas:
Busca em profundidade (depth-first search);
Busca em largura (breadth-first search)

#######
Defini 1 como parede 0 como caminho aberto 2 como entrada 3 como saida e 4 como o passo a passo que podemos visualizar percorrer o labirinto
