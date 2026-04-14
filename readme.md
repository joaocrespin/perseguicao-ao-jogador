# Perseguição com A* em Grid

Trabalho prático da disciplina de **Inteligência Artificial**: implementação do algoritmo de busca A* aplicado ao problema de perseguição de jogador por inimigo em um mapa grid.

## Problema

Um inimigo precisa encontrar o caminho ótimo até o jogador, desviando de obstáculos, usando o algoritmo A*.

## Estrutura do projeto
```
├── Node.py                    # Estrutura do nó da árvore de busca
├── BuscaNP.py                 # Buscas não informadas (amplitude, profundidade, etc.)
├── F_auxiliares.py            # Geração de grid aleatório e leitura de arquivo
├── principalBuscaSemPesos.py  # Script principal (sem pesos)
└── mapa1.txt                  # Mapa de exemplo
```
## Algoritmos implementados

**Sem peso**
- Busca em Amplitude (BFS)
- Busca em Profundidade (DFS)
- Profundidade Limitada
- Aprofundamento Iterativo
- Bidirecional

**Com peso**
- Custo Uniforme
- Greedy
- A*
- AIA*
  
## Base de código

As implementações dos algoritmos de busca (`BuscaNP.py`, `BuscaP.py` e estruturas de nó) foram disponibilizadas pelo professor como material de apoio da disciplina. A interface gráfica e a integração com o problema de perseguição foram desenvolvidas pelos integrantes.