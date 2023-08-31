import tkinter as tk
from tkinter import ttk
import Dicio

class Criar_persona():

    def __init__(self, root):

        self.janela=root

        self.frm=tk.LabelFrame(self.janela, text='Personagem:')

        #caracteristicas-------------------------------------------------------------------------------------------------
        
        self.persona=tk.LabelFrame(self.frm, text='Características:')
        
        lbl_ent_name= tk.Label (self.persona, text= 'Nome:')
        lbl_ent_name.grid(row=0, column=1, columnspan=5)

        self.name = tk.Entry (self.persona)
        self.name.grid(row = 1, column= 1, columnspan=5)

        lbl_raca = tk.Label (self.persona, text='Escolha sua raça!')
        lbl_raca.grid(row = 2, column= 1, columnspan=5)

        Raças = ['Humano', 'Elfo', 'Demonio', 'Orc']
        self.cbx_racas= ttk.Combobox(self.persona, values = Raças, state = 'readonly')
        self.cbx_racas.grid(row = 3, column= 1, columnspan=5)
        
        self.cbx_racas.bind('<<ComboboxSelected>>', self.get_attrs)

        lbl_classe = tk.Label (self.persona, text='Escolha sua classe!')
        lbl_classe.grid(row = 4, column= 1, columnspan=5)

        Classes = ['Guerreiro', 'Feiticeiro', 'Bardo', 'Ladino']
        self.cbx_classe = ttk.Combobox(self.persona, values = Classes, state = 'readonly')
        self.cbx_classe.grid(row = 5, column= 1, columnspan=5)

        self.persona.grid(row=0,column=1)
        #---------------------------------------------------------------------------------------------------------------
        
        #atributos------------------------------------------------------------------------------------------------------
        self.atributos=tk.LabelFrame(self.frm, text='Atributos')
        

        lbl_pontos = tk.Label (self.atributos, text='Distribua seus pontos!')
        lbl_pontos.grid(row = 0, column= 0, columnspan=5)

        self.var=tk.IntVar()

        self.con = tk.Spinbox(self.atributos, textvariable=self.var, from_=0, to=20, width=3)
        self.con.grid(row = 1, column= 0)

        self.var1=tk.IntVar()

        self.For = tk.Spinbox(self.atributos, textvariable=self.var1, from_=0, to=20, width=3)
        self.For.grid(row = 2, column= 0)

        self.var2=tk.IntVar()

        self.int = tk.Spinbox(self.atributos, textvariable=self.var2, from_=0, to=20, width=3)
        self.int.grid(row = 3, column= 0)

        self.var3=tk.IntVar()

        self.car = tk.Spinbox(self.atributos, textvariable=self.var3, from_=0, to=20, width=3)
        self.car.grid(row = 4, column= 0)

        self.var4=tk.IntVar()

        self.agi = tk.Spinbox(self.atributos, textvariable=self.var4, from_=0, to=20, width=3)
        self.agi.grid(row = 5, column= 0)

        self.atributos.grid(row=0,column=0)
        
        #---------------------------------------------------------------------------------------------------------------
        bnt_criar = tk.Button (self.janela, text='Criar', command=lambda: self.class_attr())
        bnt_criar.grid(row = 1, column= 0, columnspan=2, ipadx=15, pady=10)
       

        self.frm.grid(row=0, column=0)


    def get_attrs(self, event = None):
        self.Name=self.name.get()
        self.race=self.cbx_racas.get()
        self.classe=self.cbx_classe.get()
        

        attr=Dicio.RACES[self.race]

        id=0
        list_attr=[self.con, self.For, self.int, self.car, self.agi]
        list_var=[self.var, self.var1, self.var2, self.var3, self.var4, ]
        
        for value in attr.values():
            list_attr[id].config(from_=value)
            id+=1
            
            print(value)
    
        # print(attr.values())
    



        
        
        

    #def confirmar(self):
    def class_attr(self): 
        # self.get_attrs()
        attr=Dicio.RACES[self.race]
        print('---')
        

        list_attr=[self.con, self.For, self.int, self.car, self.agi]
        id=0
        # print(attr)
        # for value in attr.values():

        
