import tkinter as tk

def on_click(event):
    x, y = event.x, event.y
    print(f"Coordenadas: ({x}, {y})")

root = tk.Tk()
root.title("Captura de Coordenadas do Mouse")

# Configura a janela para modo de tela cheia
root.attributes('-fullscreen', True)

# Cria um canvas que cobre toda a tela
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Associa o evento de clique do mouse à função on_click
canvas.bind("<Button-1>", on_click)

root.mainloop()