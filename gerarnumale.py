import tkinter as tk
from tkinter import Button, Label, Toplevel
import random

class Combate():
    def Batalha(self):
        jogador = random.randint(1, 20)
        monstro = random.randint(1, 20)

        resultado = 'Você acertou seu ataque!' if jogador > monstro else 'Que pena, você errou seu ataque'

        # Cria uma nova janela para exibir o resultado
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Resultado da Batalha")

        resultado_label = Label(resultado_janela, text=resultado)
        resultado_label.pack()

        if jogador > monstro:
            self.dano_ataque_button = Button(resultado_janela, text="Gerar dano de ataque:", command=self.gerar_dano_ataque)
            self.dano_ataque_button.pack()
        else:
            self.erro_ataque_button = Button(resultado_janela, text="Gerar dano sofrido:", command=self.gerar_dano_sofrido)
            self.erro_ataque_button.pack()

    def gerar_dano_ataque(self):
        dano_ataque = random.randint(1, 20)
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Acertono ataque")
        resultado_label2 = Label(resultado_janela, text=f"Dano ataque: {dano_ataque}")
        resultado_label2.pack()

    def gerar_dano_sofrido(self):
        dano_sofrido = random.randint(1, 20)
        resultado_janela = Toplevel(self.janela)
        resultado_janela.title("Erro no Ataque")
        resultado_label3 = Label(resultado_janela, text=f"Dano sofrido: {dano_sofrido}")
        resultado_label3.pack()

    def __init__(self, root):
        self.janela = root
        self.frm = tk.LabelFrame(self.janela, text='Personagem:')
        self.name = tk.StringVar()
        self.lbl_frm_1 = tk.Label(self.frm, textvariable=self.name)
        self.lbl_frm_1.pack()
        
        self.btn_sv1 = Button(self.frm, text='Salvar Seleção', command=self.save_slct)
        self.btn_sv1.pack()
        
        bnt_alterar = Button(self.janela, text='Iniciar combate', command=self.Batalha)
        bnt_alterar.pack()

    def save_slct(self):
        print('Seleção Salva')

if __name__ == "__main__":
    janela = tk.Tk()
    combate = Combate(janela)
    janela.mainloop()
