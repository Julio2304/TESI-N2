from tkinter import * 
from tkinter.ttk import *

class Janela_mapa():
    def __init__(self, root):
        janela_mapa = root
        janela_mapa.title('Mapa')
        janela_mapa.geometry("1200x700")


        frame_mapa = Frame(janela_mapa)
        frame_mapa.pack()
        # ---   Imagens   ---
        iconeinicio = PhotoImage(file="iconmapa/inicio.png")
        iconeinimigo = PhotoImage(file='iconmapa/inimigo.png')
        iconeelite = PhotoImage(file='iconmapa/elite.png')
        iconeboss = PhotoImage(file='iconmapa/boss.png')
        iconeevento = PhotoImage(file='iconmapa/evento.png')
        iconedescanco = PhotoImage(file='iconmapa/rest.png')
        # ---    Ato 1     ---
        label_ato1 = Label(frame_mapa, text='Ato 1' , font=('Arial', 25))
        label_ato1.grid(row=0, column=3, columnspan=2)

        frame1 = Frame(frame_mapa, width=137, bg='#BBFFBB', height=610)
        frame1.grid(row=1, column=0, sticky=NS)
        buttoninicio = Button(frame1, image=iconeinicio, width=64, height=64).place(x=69, y=310, anchor=CENTER)
        frame2 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame2.grid(row=1, column=1)
        frame3 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame3.grid(row=1, column=2)
        frame4 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame4.grid(row=1, column=3)
        frame5 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame5.grid(row=1, column=4)
        frame6 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame6.grid(row=1, column=5)
        frame7 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame7.grid(row=1, column=6)
        frame8 = Frame(frame_mapa, width=137, bg='#CCCCCC', height=610)
        frame8.grid(row=1, column=7)


        

app = Tk()
janela = Janela_mapa(app)
app.mainloop()
        
