import numpy as np  
import random as rd
#-----------------------------------------------------------------------------
# GERA GRID ALEATÓRIO
#-----------------------------------------------------------------------------
def Gera_Problema_Grid_Ale(nx,ny,qtd):
    mapa = np.zeros((nx,ny),int)
    
    k = 0
    while k<qtd:
        i = rd.randrange(0,nx)
        j = rd.randrange(0,ny)
        if mapa[i][j]==0:
            mapa[i][j] = 9
            k+=1
    return mapa,nx,ny
#-----------------------------------------------------------------------------
# GERA O GRID DE ARQUIVO TEXTO
#-----------------------------------------------------------------------------
def Gera_Problema_Grid_Fixo(arquivo):
    file = open(arquivo)
    mapa = []
    for line in file:
        line = line.strip() # Remove espaços e \n
        if not line: continue # Pula linhas vazias
        
        # Converte cada caractere da linha em um inteiro
        # Antes: aux_str = line.split(",") (Isso quebrava)
        aux_int = [int(x) for x in line] 
        
        mapa.append(aux_int)
    
    nx = len(mapa)
    ny = len(mapa[0]) if nx > 0 else 0
    return mapa, nx, ny
