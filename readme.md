# Perseguição em Hyrule — A* em Grid

Trabalho prático da disciplina de **Inteligência Artificial**: implementação de algoritmos de busca aplicados ao problema de perseguição de jogador por inimigo em um mapa grid.

## Problema

Um inimigo precisa encontrar o caminho ótimo até o herói, desviando de obstáculos, utilizando diferentes algoritmos de busca em árvore.

## Estrutura do projeto

```
├── interface.py              # Interface gráfica principal
├── BuscaNP.py                # Algoritmos de busca sem peso
├── BuscaP.py                 # Algoritmos de busca com peso
├── Node.py                   # Estrutura do nó
├── NodeP.py                  # Estrutura do nó com peso
├── F_auxiliares.py           # Funções auxiliares
├── data/
│   └── mapa.txt              # Mapa do grid
├── assets/
│   ├── link.png              # Imagem do herói
│   └── octorok.png           # Imagem do inimigo
├── ReadMe.txt                # Instruções de execução
└── readme.md                 # Este arquivo
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