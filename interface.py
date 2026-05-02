import tkinter as tk
from tkinter import ttk, messagebox
from BuscaNP import buscaNP
from BuscaP import buscaP
import F_auxiliares as fa

ARQUIVO = "data/mapa.txt"
CELL    = 50

CORES = {
    "bg"     : "#0d1b0e",   
    "panel"  : "#1a2e1b",   
    "free1"  : "#4a7c3f",   
    "free2"  : "#3d6b34",  
    "wall1"  : "#5a4a2a",   
    "wall2"  : "#3d3018",  
    "path"   : "#f5c542",  
    "start"  : "#c0392b",   
    "goal"   : "#2471a3",  
    "grid"   : "#0d1b0e",
    "txt"    : "#e8d5a3",  
    "accent" : "#c9a84c",   
    "border" : "#c9a84c",
}

mapa, nx, ny = fa.Gera_Problema_Grid_Fixo(ARQUIVO)

root = tk.Tk()
root.title("Perseguição ao Jogador - Inteligência Artificial")
root.configure(bg=CORES["bg"])
root.resizable(False, False)

player_img_raw = tk.PhotoImage(file="assets/link.png")
enemy_img_raw = tk.PhotoImage(file="assets/octorok.png")

player_img = player_img_raw.subsample(11, 11) 
enemy_img = enemy_img_raw.subsample(21, 21)

# Opções
frame_ctrl = tk.Frame(root, bg=CORES["panel"], padx=15, pady=15,
                      highlightbackground=CORES["accent"], highlightthickness=2)
frame_ctrl.grid(row=0, column=0, sticky="ns", padx=(10,0), pady=10)

fonte       = ("Consolas", 10, "bold")
fonte_title = ("Consolas", 13, "bold")

# Título
tk.Label(frame_ctrl, text="Perseguição",
         font=fonte_title, bg=CORES["panel"], fg=CORES["accent"]).grid(
         row=0, column=0, sticky="w", pady=(0, 2))
tk.Label(frame_ctrl, text="Encontre o caminho do mal ao Herói",
         font=("Consolas", 8), bg=CORES["panel"], fg=CORES["txt"]).grid(
         row=1, column=0, sticky="w", pady=(0, 10))

tk.Frame(frame_ctrl, height=1, bg=CORES["accent"]).grid(
    row=2, column=0, sticky="ew", pady=(0, 10))

def titulo(txt, row):
    tk.Label(frame_ctrl, text=txt, bg=CORES["panel"], fg=CORES["txt"],
             font=fonte).grid(row=row, column=0, sticky="w", pady=(0, 4))

titulo("Método de Busca:", 3)
metodo_var = tk.StringVar(value="Amplitude")
ttk.Combobox(frame_ctrl, textvariable=metodo_var, state="readonly", width=22,
             values=["Amplitude", "Profundidade", "Prof. Limitada",
                     "Aprofund. Iterativo", "Bidirecional",
                     "Custo Uniforme", "Greedy", "A*", "AIA*"]).grid(
             row=4, column=0, sticky="w", pady=(0, 10))

titulo("Limite (Prof. Limitada / AI):", 5)
limite_var = tk.IntVar(value=5)
tk.Spinbox(frame_ctrl, from_=1, to=100, textvariable=limite_var, width=8,
           font=("Consolas", 10), bg=CORES["bg"], fg=CORES["txt"],
           buttonbackground=CORES["panel"]).grid(
           row=6, column=0, sticky="w", pady=(0, 10))

tk.Frame(frame_ctrl, height=1, bg=CORES["accent"]).grid(
    row=7, column=0, sticky="ew", pady=(0, 10))

titulo("Origem:", 8)
origem_x, origem_y = tk.IntVar(value=0), tk.IntVar(value=0)
f = tk.Frame(frame_ctrl, bg=CORES["panel"])
f.grid(row=9, column=0, sticky="w", pady=(0, 10))
tk.Spinbox(f, from_=0, to=nx-1, textvariable=origem_x, width=4,
           bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT, padx=(0, 4))
tk.Spinbox(f, from_=0, to=ny-1, textvariable=origem_y, width=4,
           bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT)

titulo("Destino:", 10)
destino_x, destino_y = tk.IntVar(value=nx-1), tk.IntVar(value=ny-1)
f2 = tk.Frame(frame_ctrl, bg=CORES["panel"])
f2.grid(row=11, column=0, sticky="w", pady=(0, 12))
tk.Spinbox(f2, from_=0, to=nx-1, textvariable=destino_x, width=4,
           bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT, padx=(0, 4))
tk.Spinbox(f2, from_=0, to=ny-1, textvariable=destino_y, width=4,
           bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT)

def executar():
    origem  = (origem_x.get(), origem_y.get())
    destino = (destino_x.get(), destino_y.get())
    metodo  = metodo_var.get()

    if mapa[origem[0]][origem[1]] != 0:
        messagebox.showerror("Erro", "O inimigo está sobre um obstáculo."); return
    if mapa[destino[0]][destino[1]] != 0:
        messagebox.showerror("Erro", "O herói está sobre um obstáculo."); return

    caminho = None
    custo   = None

    # Métodos sem peso
    if metodo in ("Amplitude", "Profundidade", "Prof. Limitada",
                  "Aprofund. Iterativo", "Bidirecional"):
        sol = buscaNP()
        if metodo == "Amplitude":
            caminho = sol.amplitude_grid(origem, destino, nx, ny, mapa)
        elif metodo == "Profundidade":
            caminho = sol.profundidade_grid(origem, destino, nx, ny, mapa)
        elif metodo == "Prof. Limitada":
            caminho = sol.prof_limitada_grid(origem, destino, nx, ny, mapa, limite_var.get())
        elif metodo == "Aprofund. Iterativo":
            caminho = sol.aprof_iterativo_grid(origem, destino, nx, ny, mapa, limite_var.get())
        elif metodo == "Bidirecional":
            caminho = sol.bidirecional_grid(origem, destino, nx, ny, mapa)
    
    # Métodos com peso
    else:
        sol = buscaP()
        if metodo == "Custo Uniforme":
            caminho, custo = sol.custo_uniforme_grid(origem, destino, mapa, nx, ny)
        elif metodo == "Greedy":
            caminho, custo = sol.greedy_grid(origem, destino, mapa, nx, ny)
        elif metodo == "A*":
            caminho, custo = sol.a_estrela_grid(origem, destino, mapa, nx, ny)
        elif metodo == "AIA*":
            caminho, custo = sol.aia_estrela_grid(origem, destino, mapa, nx, ny)

        # Fix pro caminho aparecer invertido na aba resultado na busca c/ pesos
        if caminho:
            caminho = caminho[::-1]

    txt_resultado.config(state="normal")
    txt_resultado.delete("1.0", tk.END)
    if caminho:
        txt_resultado.insert(tk.END, f"Método:  {metodo}\n")
        txt_resultado.insert(tk.END, f"Passos:  {len(caminho) - 1}\n")
        if custo is not None:
            txt_resultado.insert(tk.END, f"Custo:   {custo}\n")
        txt_resultado.insert(tk.END, "\nCaminho:\n")
        txt_resultado.insert(tk.END, " -> ".join(str(p) for p in caminho))
        desenhar_grid(caminho, origem, destino)
    else:
        txt_resultado.insert(tk.END, "Caminho não encontrado.")
        desenhar_grid([], origem, destino)
    txt_resultado.config(state="disabled")

tk.Button(frame_ctrl, text="▶  INICIAR BUSCA", command=executar,
          bg=CORES["accent"], fg=CORES["bg"],
          activebackground="#a8892e", activeforeground=CORES["bg"],
          font=("Consolas", 11, "bold"), relief="flat",
          padx=8, pady=8, cursor="hand2").grid(
          row=12, column=0, sticky="ew", pady=8)

tk.Frame(frame_ctrl, height=1, bg=CORES["accent"]).grid(
    row=13, column=0, sticky="ew", pady=(0, 8))

tk.Label(frame_ctrl, text="Resultado:", font=fonte,
         bg=CORES["panel"], fg=CORES["txt"]).grid(row=14, column=0, sticky="w")

txt_resultado = tk.Text(frame_ctrl, width=30, height=12,
                        bg="#0a120a", fg=CORES["txt"],
                        font=("Consolas", 9),
                        state="disabled", relief="flat",
                        insertbackground=CORES["txt"])
txt_resultado.grid(row=15, column=0, pady=(4, 0))

# Grid
frame_grid = tk.Frame(root, bg=CORES["bg"], padx=12, pady=10)
frame_grid.grid(row=0, column=1, sticky="n")

canvas = tk.Canvas(frame_grid, width=ny*CELL, height=nx*CELL,
                   bg=CORES["bg"], highlightthickness=2,
                   highlightbackground=CORES["accent"])
canvas.pack()

# Legenda
tk.Frame(frame_grid, height=1, bg=CORES["accent"]).pack(fill="x", pady=10)
tk.Label(frame_grid, text="Legenda:", font=("Consolas", 10, "bold"),
         bg=CORES["bg"], fg=CORES["accent"]).pack(anchor="w")

frame_leg = tk.Frame(frame_grid, bg=CORES["bg"])
frame_leg.pack(anchor="w", pady=(4, 0))

def leg_item(cor, texto):
    f = tk.Frame(frame_leg, bg=CORES["bg"])
    f.pack(side=tk.LEFT, padx=(0, 14))
    tk.Frame(f, width=14, height=14, bg=cor,
             highlightbackground=CORES["accent"], highlightthickness=1).pack(side=tk.LEFT, padx=(0, 5))
    tk.Label(f, text=texto, font=("Consolas", 9),
             bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT)

leg_item(CORES["start"], "Inimigo")
leg_item(CORES["goal"],  "Herói")
leg_item(CORES["path"],  "Trilha")
leg_item(CORES["wall1"], "Rocha")
leg_item(CORES["free1"], "Campo")

def desenhar_bloco(x1, y1, cor1, cor2):
    canvas.create_rectangle(x1, y1, x1+CELL, y1+CELL,
                            fill=cor1, outline=CORES["grid"])
    canvas.create_rectangle(x1+3, y1+3, x1+CELL-3, y1+CELL-3,
                            fill=cor2, outline="")

def desenhar_grid(caminho=[], origem=None, destino=None):
    canvas.delete("all")
    caminho_set = set(map(tuple, caminho))
    for i in range(nx):
        for j in range(ny):
            x1, y1 = j*CELL, i*CELL
            pos = (i, j)
            if mapa[i][j] != 0:
                # Rocha com textura
                desenhar_bloco(x1, y1, CORES["wall1"], CORES["wall2"])
                canvas.create_text(x1+CELL//2, y1+CELL//2,
                                   text="▪", font=("Consolas", 18),
                                   fill="#6b5a3a")
            elif pos in caminho_set:
                # Trilha dourada
                desenhar_bloco(x1, y1, "#d4a017", CORES["path"])
                canvas.create_text(x1+CELL//2, y1+CELL//2,
                                   text="◆", font=("Consolas", 10),
                                   fill="#fffacd")
            else:
                # Grama xadrez
                cor = CORES["free1"] if (i+j) % 2 == 0 else CORES["free2"]
                desenhar_bloco(x1, y1, cor, cor)

            # Coordenadas
            txt_cor = "#c9a84c" if mapa[i][j] != 0 else "#1a3d1a"
            canvas.create_text(x1+3, y1+3, text=f"{i},{j}",
                               anchor="nw", fill=txt_cor,
                               font=("Consolas", 6, "bold"))
            # Personagens
            if pos == origem:
                canvas.create_rectangle(x1+4, y1+4, x1+CELL-4, y1+CELL-4,
                                        fill=CORES["start"], outline="")
                canvas.create_image(x1+CELL//2, y1+CELL//2, image=enemy_img)
            elif pos == destino:
                canvas.create_rectangle(x1+4, y1+4, x1+CELL-4, y1+CELL-4,
                                        fill=CORES["goal"], outline="")
                canvas.create_image(x1+CELL//2, y1+CELL//2, image=player_img)

desenhar_grid()
root.mainloop()