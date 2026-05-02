import tkinter as tk
from tkinter import ttk, messagebox
from BuscaNP import buscaNP
from BuscaP import buscaP
import F_auxiliares as fa

ARQUIVO = "mapa1.txt"
CELL    = 50

CORES = {
    "bg"     : "#1e1e2e",
    "panel"  : "#2b2d42",
    "free1"  : "#8ec07c",
    "free2"  : "#7cb36d",
    "wall1"  : "#5c677d",
    "wall2"  : "#434c5e",
    "path"   : "#f9c74f",
    "start"  : "#00a8ff",
    "goal"   : "#ef476f",
    "grid"   : "#000000",
    "txt"    : "#f1f1f1",
    "border" : "#CCCCCC",
}

mapa, nx, ny = fa.Gera_Problema_Grid_Fixo(ARQUIVO)

root = tk.Tk()
root.title("Perseguição ao Jogador - Inteligência Artificial")
root.configure(bg=CORES["bg"])
root.resizable(False, False)

player_img = tk.PhotoImage(file="amigo.png")
enemy_img  = tk.PhotoImage(file="inimigo.png")

# ── PAINEL ESQUERDO ──────────────────────────
frame_ctrl = tk.Frame(root, bg=CORES["panel"], padx=15, pady=15)
frame_ctrl.grid(row=0, column=0, sticky="ns")

fonte = ("Consolas", 10, "bold")

def titulo(txt, row):
    tk.Label(frame_ctrl, text=txt, bg=CORES["panel"], fg="white",
             font=fonte).grid(row=row, column=0, sticky="w", pady=(0, 4))

titulo("Método:", 0)
metodo_var = tk.StringVar(value="Amplitude")
ttk.Combobox(frame_ctrl, textvariable=metodo_var, state="readonly", width=22,
             values=["Amplitude", "Profundidade", "Prof. Limitada",
                     "Aprofund. Iterativo", "Bidirecional",
                     "Custo Uniforme", "Greedy", "A*", "AIA*"]).grid(
             row=1, column=0, sticky="w", pady=(0, 10))

titulo("Limite (Prof. Limitada / AI):", 2)
limite_var = tk.IntVar(value=5)
tk.Spinbox(frame_ctrl, from_=1, to=100, textvariable=limite_var, width=8,
           font=("Consolas", 10)).grid(row=3, column=0, sticky="w", pady=(0, 10))

titulo("Origem:", 4)
origem_x, origem_y = tk.IntVar(value=0), tk.IntVar(value=0)
f = tk.Frame(frame_ctrl, bg=CORES["panel"])
f.grid(row=5, column=0, sticky="w", pady=(0, 10))
tk.Spinbox(f, from_=0, to=nx-1, textvariable=origem_x, width=4).pack(side=tk.LEFT, padx=(0, 4))
tk.Spinbox(f, from_=0, to=ny-1, textvariable=origem_y, width=4).pack(side=tk.LEFT)

titulo("Destino:", 6)
destino_x, destino_y = tk.IntVar(value=nx-1), tk.IntVar(value=ny-1)
f2 = tk.Frame(frame_ctrl, bg=CORES["panel"])
f2.grid(row=7, column=0, sticky="w", pady=(0, 12))
tk.Spinbox(f2, from_=0, to=nx-1, textvariable=destino_x, width=4).pack(side=tk.LEFT, padx=(0, 4))
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

    txt_resultado.config(state="normal")
    txt_resultado.delete("1.0", tk.END)
    if caminho:
        txt_resultado.insert(tk.END, f"Metodo: {metodo}\n")
        txt_resultado.insert(tk.END, f"Passos: {len(caminho) - 1}\n")
        if custo is not None:
            txt_resultado.insert(tk.END, f"Custo:  {custo}\n")
        txt_resultado.insert(tk.END, "\nCaminho:\n")
        txt_resultado.insert(tk.END, " -> ".join(str(p) for p in caminho))
        desenhar_grid(caminho, origem, destino)
    else:
        txt_resultado.insert(tk.END, "Sem caminho encontrado.")
        desenhar_grid([], origem, destino)
    txt_resultado.config(state="disabled")

tk.Button(frame_ctrl, text="▶ EXECUTAR", command=executar,
          bg="#ff006e", fg="white", activebackground="#d90429", activeforeground="white",
          font=("Consolas", 11, "bold"), relief="flat",
          padx=8, pady=8, cursor="hand2").grid(
          row=8, column=0, sticky="ew", pady=8)

txt_resultado = tk.Text(frame_ctrl, width=30, height=14,
                        bg="#111111", fg="white", font=("Consolas", 9),
                        state="disabled", relief="flat")
txt_resultado.grid(row=10, column=0, pady=(10, 0))

# ── GRID VISUAL ──────────────────────────────
frame_grid = tk.Frame(root, bg=CORES["bg"], padx=12, pady=12)
frame_grid.grid(row=0, column=1, sticky="n")

canvas = tk.Canvas(frame_grid, width=ny*CELL, height=nx*CELL,
                   bg="#111111", highlightthickness=0)
canvas.pack()

# Legenda
tk.Frame(frame_grid, height=1, bg=CORES["border"]).pack(fill="x", pady=12)
tk.Label(frame_grid, text="Legenda:", font=("Consolas", 10, "bold"),
         bg=CORES["bg"], fg=CORES["txt"]).pack(anchor="w")

frame_leg = tk.Frame(frame_grid, bg=CORES["bg"])
frame_leg.pack(anchor="w", pady=(4, 0))

def leg_item(cor, texto):
    f = tk.Frame(frame_leg, bg=CORES["bg"])
    f.pack(side=tk.LEFT, padx=(0, 12))
    tk.Frame(f, width=14, height=14, bg=cor).pack(side=tk.LEFT, padx=(0, 6))
    tk.Label(f, text=texto, font=("Consolas", 9),
             bg=CORES["bg"], fg=CORES["txt"]).pack(side=tk.LEFT)

leg_item(CORES["start"], "Origem (S)")
leg_item(CORES["goal"],  "Destino (G)")
leg_item(CORES["path"],  "Caminho encontrado")
leg_item(CORES["wall1"], "Obstáculo")
leg_item(CORES["free1"], "Livre")

# ── DESENHA O GRID ────────────────────────────
def desenhar_bloco_pixel(x1, y1, cor1, cor2):
    canvas.create_rectangle(x1, y1, x1+CELL, y1+CELL,
                            fill=cor1, outline=CORES["grid"])
    canvas.create_rectangle(x1+4, y1+4, x1+CELL-4, y1+CELL-4,
                            fill=cor2, outline="")

def desenhar_grid(caminho=[], origem=None, destino=None):
    canvas.delete("all")
    caminho_set = set(map(tuple, caminho))

    for i in range(nx):
        for j in range(ny):
            x1, y1 = j*CELL, i*CELL
            pos = (i, j)

            if mapa[i][j] != 0:
                desenhar_bloco_pixel(x1, y1, CORES["wall1"], CORES["wall2"])
            elif pos in caminho_set:
                desenhar_bloco_pixel(x1, y1, "#ffd166", CORES["path"])
            else:
                cor = CORES["free1"] if (i+j) % 2 == 0 else CORES["free2"]
                desenhar_bloco_pixel(x1, y1, cor, cor)

            # Coordenadas
            txt_cor = "#ffffff" if mapa[i][j] != 0 else "#222222"
            canvas.create_text(x1+4, y1+4, text=f"{i},{j}",
                               anchor="nw", fill=txt_cor,
                               font=("Consolas", 7, "bold"))

            # Personagens
            if pos == origem:
                canvas.create_image(x1+CELL//2, y1+CELL//2, image=enemy_img)
            elif pos == destino:
                canvas.create_image(x1+CELL//2, y1+CELL//2, image=player_img)

desenhar_grid()
root.mainloop()