from tkinter import *
from ttkbootstrap import Style
from Cadastro_user import Cadastro_user as User
from Saves import Saves as save

class TelaPrincipal:


    def __init__(self, master):
        self.janela = master
        self.janela.title("Death's Valley")
        
        self.style = Style('superhero')
        
        self.frm_principal = Frame(self.janela)
        self.frm_principal.grid(row=0, column=0, padx=20, pady=20)

        self.login()

    def login(self):

        self.limpar_tela()
        lbl = Label(self.frm_principal, text="Bem-vindo(a) ao Death's Valley")
        lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.ent_user = Entry(self.frm_principal)
        self.ent_user.grid(row=1, column=1, padx=10, pady=5)
        lbl_user = Label(self.frm_principal, text='Usuário:')
        lbl_user.grid(row=1, column=0, padx=10, pady=5)
        
        self.ent_senha = Entry(self.frm_principal, show='*')
        self.ent_senha.grid(row=2, column=1, padx=10, pady=5)
        lbl_senha = Label(self.frm_principal, text='Senha:')
        lbl_senha.grid(row=2, column=0, padx=10, pady=5)
        
        btn_logar = Button(self.frm_principal, text='Entrar', command=self.saves, width=15)
        btn_logar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        btn_cadastrar=Button(self.frm_principal, text='Cadastrar',command=self.cadastrar, width=15)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        self.limpar_tela()
        User(self.frm_principal)
        
    def logar(self):
        self.limpar_tela()

        btn_voltar_menu=Button(self.frm_principal, text='Sair', command=self.login)
        btn_voltar_menu.grid(row=1,column=0)
    
    def saves(self):
        self.limpar_tela()
        save(self.frm_principal)

        btn_voltar_menu=Button(self.frm_principal, text='Voltar', command=self.login)
        btn_voltar_menu.grid(row=1,column=1, columnspan=2, rowspan=2, padx=5, pady=5)

    def limpar_tela(self):
        for widget in self.frm_principal.winfo_children():
            widget.destroy()

app = Tk()
janela = TelaPrincipal(app)
app.mainloop()
