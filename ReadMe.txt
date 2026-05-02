================================================
 PERSEGUIÇÃO AO JOGADOR - INTELIGÊNCIA ARTIFICIAL
================================================

Trabalho prático da disciplina de Inteligência Artificial
Faculdade de Tecnologia de Cruzeiro - 6º ADS


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
 ESTRUTURA DE PASTAS
------------------------------------------------

  /
  ├── interface.py
  ├── BuscaNP.py
  ├── BuscaP.py
  ├── Node.py
  ├── NodeP.py
  ├── F_auxiliares.py
  ├── data/
  │   └── mapa.txt
  └── assets/
      ├── link.png
      └── octorok.png


------------------------------------------------
 COMO USAR A INTERFACE
------------------------------------------------

1. MÉTODO: selecione o algoritmo de busca desejado
   no menu suspenso. Opções disponíveis:
   Amplitude, Profundidade, Prof. Limitada,
   Aprofund. Iterativo, Bidirecional,
   Custo Uniforme, Greedy, A*, AIA*

2. LIMITE: usado apenas pelos métodos "Prof. Limitada"
   e "Aprofund. Iterativo". Define a profundidade máxima
   da busca.

3. ORIGEM: coordenadas (linha, coluna) do inimigo.
   Representa o estado inicial da busca.

4. DESTINO: coordenadas (linha, coluna) do herói.
   Representa o estado objetivo da busca.

5. Clique em "INICIAR BUSCA" para executar.

6. O caminho encontrado será exibido como trilha
   dourada no mapa. A área de resultado mostra o
   método utilizado, número de passos e custo total.
   Para caminhos longos, pode ser necessário rolar
   a área de resultado para visualizar o trajeto
   completo.


------------------------------------------------
 FORMATO DO MAPA (data/mapa.txt)
------------------------------------------------

O mapa é um grid 15x15 onde:
  0 = célula livre
  9 = obstáculo (rocha)

Os valores de cada linha são separados por vírgula.
Exemplo:
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
  0,0,0,9,0,0,0,0,0,0,0,0,0,9,0
  ...

O mapa pode ser modificado editando o arquivo
data/mapa.txt. Para alterar o tamanho do grid,
basta adicionar ou remover linhas e colunas,
mantendo sempre o mesmo número de colunas
por linha e os valores separados por vírgula.


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