import tkinter as tk
from tkinter import ttk, messagebox
from BuscaNP import buscaNP
from BuscaP import buscaP
import F_auxiliares as fa

ARQUIVO = "mapa1.txt"
CELL    = 50

CORES = {
    "free"   : "white",
    "wall"   : "#555555",
    "start"  : "#2D7DD2",
    "goal"   : "#E05C2E",
    "path"   : "#F9D040",
    "border" : "#CCCCCC",
}

mapa, nx, ny = fa.Gera_Problema_Grid_Fixo(ARQUIVO)

root = tk.Tk()
root.title("Perseguição ao Jogador - Inteligência Artificial")
root.resizable(False, False)
player_img = tk.PhotoImage(file="amigo.png")
enemy_img = tk.PhotoImage(file="inimigo.png")

# Opções
frame_ctrl = tk.Frame(root, padx=10, pady=10)
frame_ctrl.grid(row=0, column=0, sticky="ns")

tk.Label(frame_ctrl, text="Método:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
metodo_var = tk.StringVar(value="Amplitude")
ttk.Combobox(frame_ctrl, textvariable=metodo_var, state="readonly", width=22,
             values=["Amplitude", "Profundidade", "Prof. Limitada",
                     "Aprofund. Iterativo", "Bidirecional",
                     "Custo Uniforme", "Greedy", "A*", "AIA*"]).grid(
             row=1, column=0, sticky="w", pady=(0, 10))

tk.Label(frame_ctrl, text="Limite (Prof. Limitada / AI):", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
limite_var = tk.IntVar(value=5)
tk.Spinbox(frame_ctrl, from_=1, to=100, textvariable=limite_var, width=6).grid(
    row=3, column=0, sticky="w", pady=(0, 10))

tk.Label(frame_ctrl, text="Origem:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w")
origem_x, origem_y = tk.IntVar(value=0), tk.IntVar(value=0)
f = tk.Frame(frame_ctrl); f.grid(row=5, column=0, sticky="w", pady=(0, 10))
tk.Spinbox(f, from_=0, to=nx-1, textvariable=origem_x, width=4).pack(side=tk.LEFT, padx=(0,4))
tk.Spinbox(f, from_=0, to=ny-1, textvariable=origem_y, width=4).pack(side=tk.LEFT)

tk.Label(frame_ctrl, text="Destino:", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
destino_x, destino_y = tk.IntVar(value=nx-1), tk.IntVar(value=ny-1)
f2 = tk.Frame(frame_ctrl); f2.grid(row=7, column=0, sticky="w", pady=(0, 16))
tk.Spinbox(f2, from_=0, to=nx-1, textvariable=destino_x, width=4).pack(side=tk.LEFT, padx=(0,4))
tk.Spinbox(f2, from_=0, to=ny-1, textvariable=destino_y, width=4).pack(side=tk.LEFT)

def executar():
    origem  = (origem_x.get(), origem_y.get())
    destino = (destino_x.get(), destino_y.get())
    metodo  = metodo_var.get()

    if mapa[origem[0]][origem[1]] != 0:
        messagebox.showerror("Erro", "Origem está sobre um obstáculo."); return
    if mapa[destino[0]][destino[1]] != 0:
        messagebox.showerror("Erro", "Destino está sobre um obstáculo."); return

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

    txt.config(state="normal")
    txt.delete("1.0", tk.END)
    if caminho:
        txt.insert(tk.END, f"Método: {metodo}\n")
        txt.insert(tk.END, f"Caminho: {caminho}\n")
        if custo is not None:
            txt.insert(tk.END, f"Custo: {custo}")
        else:
            txt.insert(tk.END, f"Custo: {len(caminho) - 1} passos")
        desenhar_grid(caminho, origem, destino)
    else:
        txt.insert(tk.END, "Caminho não encontrado.")
        desenhar_grid([], origem, destino)
    txt.config(state="disabled")

tk.Button(frame_ctrl, text="Executar", font=("Arial", 11, "bold"),
          bg="#2D7DD2", fg="white", padx=10, pady=6,
          relief=tk.FLAT, cursor="hand2", command=executar).grid(
          row=8, column=0, sticky="ew", pady=(0, 12))

tk.Label(frame_ctrl, text="Resultado:", font=("Arial", 10, "bold")).grid(row=9, column=0, sticky="w")
txt = tk.Text(frame_ctrl, width=28, height=6, state="disabled",
              font=("Courier", 9), relief=tk.SUNKEN, bd=1)
txt.grid(row=10, column=0, pady=(4, 0))

# Grid
frame_grid = tk.Frame(root, padx=10, pady=10)
frame_grid.grid(row=0, column=1, sticky="n")

canvas = tk.Canvas(frame_grid, width=ny*CELL, height=nx*CELL,
                   bg="white", relief=tk.SUNKEN, bd=1)
canvas.pack()

# Legenda
tk.Frame(frame_grid, height=1, bg="#CCCCCC").pack(fill="x", pady=12)
tk.Label(frame_grid, text="Legenda:", font=("Arial", 10, "bold")).pack(anchor="w")

frame_leg = tk.Frame(frame_grid)
frame_leg.pack(anchor="w", pady=(4, 0))

def leg_item(cor, texto):
    f = tk.Frame(frame_leg)
    f.pack(side=tk.LEFT, padx=(0, 12))
    tk.Frame(f, width=14, height=14, bg=cor, relief=tk.FLAT).pack(side=tk.LEFT, padx=(0, 6))
    tk.Label(f, text=texto, font=("Arial", 9)).pack(side=tk.LEFT)

leg_item(CORES["start"], "Origem (S)")
leg_item(CORES["goal"],  "Destino (G)")
leg_item(CORES["path"],  "Caminho encontrado")
leg_item(CORES["wall"],  "Obstáculo")
leg_item(CORES["free"],  "Livre")

def desenhar_grid(caminho=[], origem=None, destino=None):
    canvas.delete("all")
    caminho_set = set(map(tuple, caminho))
    for i in range(nx):
        for j in range(ny):
            x1, y1 = j*CELL, i*CELL
            pos = (i, j)
            if pos == origem:        cor = CORES["start"]
            elif pos == destino:     cor = CORES["goal"]
            elif mapa[i][j] != 0:   cor = CORES["wall"]
            elif pos in caminho_set: cor = CORES["path"]
            else:                    cor = CORES["free"]

            canvas.create_rectangle(x1, y1, x1+CELL, y1+CELL,
                                    fill=cor, outline=CORES["border"])

            cor_txt = "white" if cor in (CORES["wall"], CORES["start"], CORES["goal"]) else "#AAAAAA"
            canvas.create_text(x1+3, y1+3, text=f"{i},{j}",
                               anchor="nw", font=("Arial", 7), fill=cor_txt)

            if pos == origem:
                canvas.create_image(
                    x1 + CELL//2,
                    y1 + CELL//2,
                    image=enemy_img
                )

            elif pos == destino:
                canvas.create_image(
                    x1 + CELL//2,
                    y1 + CELL//2,
                    image=player_img
                )

desenhar_grid()
root.mainloop()