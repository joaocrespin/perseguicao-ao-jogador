================================================
 PERSEGUIÇÃO AO JOGADOR — INTELIGÊNCIA ARTIFICIAL
================================================

Trabalho prático da disciplina de Inteligência Artificial
Faculdade de Tecnologia de Cruzeiro — 6º ADS


------------------------------------------------
 REQUISITOS
------------------------------------------------

Python 3.13
Download: https://www.python.org/downloads/


------------------------------------------------
 INSTALAÇÃO (com ambiente virtual)
------------------------------------------------

1. Abra o terminal na pasta do projeto

2. Crie o ambiente virtual:
     python -m venv venv

3. Ative o ambiente virtual:

   Windows:
     venv\Scripts\activate

   Linux/Mac:
     source venv/bin/activate

4. Instale as dependências:
     pip install numpy

5. Execute a interface:
     python interface.py

Para desativar o ambiente virtual quando terminar:
  deactivate


------------------------------------------------
 ARQUIVOS DO PROJETO
------------------------------------------------

interface.py              — Interface gráfica principal
BuscaNP.py                — Algoritmos de busca sem peso
BuscaP.py                 — Algoritmos de busca com peso
Node.py                   — Estrutura do nó
NodeP.py                  — Estrutura do nó com peso
F_auxiliares.py           — Funções auxiliares
mapa1.txt                 — Mapa do grid 10x10
principalBuscaSemPesos.py — Script de terminal (sem pesos)
principalBuscaComPesos.py — Script de terminal (com pesos)


------------------------------------------------
 COMO USAR A INTERFACE
------------------------------------------------

1. MÉTODO: selecione o algoritmo de busca desejado
   no menu suspenso.

2. LIMITE: usado apenas pelos métodos "Prof. Limitada"
   e "Aprofund. Iterativo". Define a profundidade máxima
   da busca.

3. ORIGEM: coordenadas (linha, coluna) do inimigo (S).

4. DESTINO: coordenadas (linha, coluna) do jogador (G).

5. Clique em "Executar" para iniciar a busca.

6. O caminho encontrado será exibido em amarelo no mapa
   e detalhado na área de resultado com o custo total.


------------------------------------------------
 FORMATO DO MAPA (mapa1.txt)
------------------------------------------------

O mapa é um grid 10x10 onde:
  0 = célula livre
  9 = obstáculo

Os valores de cada linha são separados por vírgula.
Exemplo:
  0,0,0,0,0,0,0,0,0,0
  0,0,0,9,0,0,0,0,0,0
  ...


------------------------------------------------
 ALGORITMOS DISPONÍVEIS
------------------------------------------------

Sem peso (BuscaNP.py):
  - Amplitude
  - Profundidade
  - Profundidade Limitada
  - Aprofundamento Iterativo
  - Bidirecional

Com peso (BuscaP.py):
  - Custo Uniforme
  - Greedy
  - A*
  - AIA*

================================================