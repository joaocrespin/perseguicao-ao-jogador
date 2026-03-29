from BuscaNP import buscaNP
import F_auxiliares as fa



#---------------- Executa Grid ------------------------------
arquivo = "mapa1.txt"
mapa,dx,dy = fa.Gera_Problema_Grid_Fixo(arquivo)

# Entrada de dados para busca em grid
origem  = tuple(map(int, input("Digite a origem (x y): ").split()))
destino = tuple(map(int, input("Digite o destino (x y): ").split()))
#destino_str = input("Digite as coordenadas de destino no formato x y, separadas por vírgula: ")
#destino = [tuple(map(int, coord.split())) for coord in destino_str.split(",")]

flag_origem  = (0<=origem[0]<dx)  and (0<=origem[1]<dy)  and (mapa[origem[0]][origem[1]]==0)
flag_destino = (0<=destino[0]<dx) and (0<=destino[1]<dy) and (mapa[destino[0]][destino[1]]==0)
#flag_destino = all(0<=x<dx and 0<=y<dy for x,y in destino)
flag = flag_origem and flag_destino
#------------------------------------------------------------

print(f"DEBUG: dx={dx}, dy={dy}")
print(f"DEBUG: Valor na origem {origem}: {mapa[origem[0]][origem[1]]}")
print(f"DEBUG: Valor no destino {destino}: {mapa[destino[0]][destino[1]]}")
print(f"DEBUG: flag_origem={flag_origem}, flag_destino={flag_destino}")


if flag:
    sol = buscaNP()
    caminho = []
    #caminho = sol.amplitude(origem,destino,nos,grafo)
    caminho = sol.amplitude(origem,destino,dx,dy,mapa)
    if caminho!=None:
        print("\n*****AMPLITUDE*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")

    #caminho = sol.profundidade(origem,destino,nos,grafo)
    caminho = sol.profundidade(origem,destino,dx,dy,mapa)
    print("\n*****PROFUNDIDADE*****")
    if caminho!=None:
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")
 
    # limite = 2
    # caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
    # print("\n*****PROFUNDIDADE LIMITADA*****")
    # if caminho!=None:
    #     print("\n*****PROFUNDIDADE LIMITADA*****")
    #     print("Caminho: ",caminho)
    #     print("Custo..: ",len(caminho)-1)
    # else:
    #     print("CAMINHO NÃO ENCONTRADO")
    
    # limite = 3
    # caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
    # print("\n*****PROFUNDIDADE LIMITADA*****")
    # if caminho!=None:
    #     print("Caminho: ",caminho)
    #     print("Custo..: ",len(caminho)-1)
    # else:
    #     print("CAMINHO NÃO ENCONTRADO")
    
    # limite = 4
    # caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
    # print("\n*****PROFUNDIDADE LIMITADA*****")
    # if caminho!=None:
    #     print("Caminho: ",caminho)
    #     print("Custo..: ",len(caminho)-1)
    # else:
    #     print("CAMINHO NÃO ENCONTRADO")

    # l_max = len(nos)
    # caminho = sol.aprof_iterativo(origem,destino,nos,grafo,l_max)
    # if caminho!=None:
    #     print("\n*****APROFUNDAMENTO ITERATIVO*****")
    #     print("Caminho: ",caminho)
    #     print("Custo..: ",len(caminho)-1)
    # else:
    #     print("CAMINHO NÃO ENCONTRADO")
       
    # caminho = sol.bidirecional(origem,destino,nos,grafo)
    # if caminho!=None:
    #     print("\n*****BIDIRECIONAL*****")
    #     print("Caminho: ",caminho)
    #     print("Custo..: ",len(caminho)-1)
    # else:
    #     print("CAMINHO NÃO ENCONTRADO")
