import tkinter as tk

root = tk.Tk()
root.title("Meu Programa Tkinter")

label = tk.Label(root, text="Olá, Tkinter!")
label.pack()

button = tk.Button(root, text="Clique Aqui", command=lambda: print("Botão clicado!"))
button.pack()

root.mainloop()


