import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

lbl_raca = tk.Label (janela, text='Escolha sua raça!')
lbl_raca.grid(row = 0, column= 0, columnspan=5)

lista1 = ['Humano', 'Elfo', 'Demonio', 'Orc']
cbx = ttk.Combobox(janela, values = lista1, state = 'readonly')
cbx.grid(row = 1, column= 0, columnspan=5)

lbl_classe = tk.Label (janela, text='Escolha sua classe!')
lbl_classe.grid(row = 3, column= 0, columnspan=5)

lista2 = ['Guerreiro', 'Feiticeiro', 'Bardo', 'Ladino']
cbx = ttk.Combobox(janela, values = lista2, state = 'readonly')
cbx.grid(row = 4, column= 0, columnspan=5)

lbl_pontos = tk.Label (janela, text='Distribua seus pontos!')
lbl_pontos.grid(row = 5, column= 0, columnspan=5)

lbl_pontosdesc = tk.Label (janela, text='(Seus atributos iniciais se alteram conforme a raça e classe escolhidos)')
lbl_pontosdesc.grid(row = 6, column= 0, columnspan=5)

spb_const = tk.Spinbox(janela, from_=0, to=8, wrap=True, width=3)
spb_const.grid(row = 7, column= 0)

spb_forca = tk.Spinbox(janela, from_=0, to=8, wrap=True, width=3)
spb_forca.grid(row = 7, column= 1)

spb_int = tk.Spinbox(janela, from_=0, to=8, wrap=True, width=3)
spb_int.grid(row = 7, column= 2)

spb_caris = tk.Spinbox(janela, from_=0, to=8, wrap=True, width=3)
spb_caris.grid(row = 7, column= 3)

spb_agil = tk.Spinbox(janela, from_=0, to=8, wrap=True, width=3)
spb_agil.grid(row = 7, column= 4, columnspan=5)


bnt_criar = tk.Button (janela, text='Criar personagem', command=janela.destroy)
bnt_criar.grid(row = 8, column= 0, columnspan=5)

janela.mainloop()
