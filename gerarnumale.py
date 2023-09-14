from tkinter import *
import random

bnt_alterar = Button (janela, text='Iniciar combate', command=janela.destroy)
bnt_alterar.grid(row = 8, column= 0, columnspan=5)

sorteio1 = random.randint(1, 20)
sorteio2 = random.randint(1, 20)


if sorteio1 > sorteio2:
    print('Você acertou seu ataque!')
else:
    print('Que pena, você errou seu ataque')
    print(sorteio)