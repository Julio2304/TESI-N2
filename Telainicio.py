import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

#Frame 0
frame0 = tk.LabelFrame(janela, text="Você é um:")
frame0.grid(row=0, column=0)

lbl_suaraca = tk.Label(frame0, text="ORC")
lbl_suaraca.pack()

#Frame 1
frame1 = tk.LabelFrame(janela, text="A classe escolhida foi:")
frame1.grid(row=0, column=1)

lbl_suaclasse = tk.Label(frame1, text="GUERREIRO")
lbl_suaclasse.pack()

#Frame 2
frame2 = tk.LabelFrame(janela, text="Pontos de atributos:")
frame2.grid(row=1, column=0, columnspan=2)

lbl_vocepontos = tk.Label (frame2, text='Seus pontos distribuidos estão abaixo:')
lbl_vocepontos.grid(row=1, column=0, columnspan=5)

lbl_novospontos = tk.Label (frame2, text='Ao derrotar monstros você ganha mais pontos para redistribuir.')
lbl_novospontos.grid(row=2, column=0, columnspan=5)

spb_const = tk.Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
spb_const.grid(row=3, column=0)

spb_forca = tk.Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
spb_forca.grid(row=3, column=1)

spb_int = tk.Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
spb_int.grid(row=3, column=2)

spb_caris = tk.Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
spb_caris.grid(row=3, column=3)

spb_agil = tk.Spinbox(frame2, from_=0, to=8, wrap=True, width=3)
spb_agil.grid(row=3, column=4, columnspan=5)




bnt_alterar = tk.Button (janela, text='Confirmar alterações', command=janela.destroy)
bnt_alterar.grid(row = 8, column= 0, columnspan=5)

janela.mainloop()
