import tkinter as tk
from tkinter import ttk
import datetime as dt

janela = tk.Tk()

janela.title("Cadastro")
label_descricao = tk.Label(text="Descrição")
label_descricao.grid(row=1, column=0,padx=10,pady=10,sticky="nswe", columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2,column=0,padx=10,pady=10,sticky="nswe",columnspan=1)

janela.mainloop()
