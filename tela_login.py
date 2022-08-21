from tkinter import *
import os
from tkinter.font import BOLD
from turtle import width

# criação de arquivo de texto

c = os.path.dirname(__file__)
nomeArquivo = c+'\\nomes.txt'

# Função para salvar dados

def gravarDados():

    arquivos=open(nomeArquivo, 'a')
    arquivos.write(f'Usuário: {unome.get()}')
    arquivos.write(f'\nSenha: {usenha.get()}')
    arquivos.write('\n\n')
    arquivos.close

# Inicio do programa
 
pg = Tk() 

pg.title('Login') # Título da pag

pg.geometry('500x550') # Dimensões da pag

pg.resizable(False, False) # Não redimensionavel

pg.configure(background='#ffffff') # Cor de fundo 

pg.iconbitmap('tela_login\logo\senac750.ico') # Ícone do programa

'''
anchor = N = Norte S, = Sul, E = Leste, W = Oeste.

NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Entry = Única linha

Text =  múltiplas linhas

'''
# Imagem 
logo = PhotoImage(file='tela_login\logo\senac750.png')
logo = logo.subsample(2, 2)
figura1 = Label(image=logo, bg='#ffffff')

figura1.grid(row = 0, column=0, padx = (65,0), pady=(30,0))

# Usuário
usu = Label(pg, text='Usuário:', font=('Arial', 12, BOLD), background='#ffffff',foreground='#03588C', anchor=W) # Cores, fontes, cor de fundo, cor da letra

usu.place(x=160, y=300, width=100, height=20) # Medidas da caixa 

unome = Entry(pg) # Entrada de dados

unome.place(x = 160, y = 325, width=200, height=20) # Medidas da caixa

# Senha
senh = Label(pg, text='Senha', font=('Arial', 12, BOLD),background='#ffffff', foreground='#03588C', anchor=W) # Cores, fontes, cor de fundo, cor da letra

senh.place(x=160, y=360, width=100, height=20)

usenha = Entry(pg)

usenha.place(x = 160, y = 385, width=200, height=20)

# Esqueceu a senha?

esq = Button(pg, text='Esqueceu a senha?', font=('Arial', 12, BOLD),background='#ffffff', foreground='#03588C', anchor=W) # Cores, fontes, cor de fundo, cor da letra

esq.place(x=160, y=430, width=160, height=20)

# Botão
but = Button(pg, text='Salvar', font=('Arial', 12),
bg='#03588C', foreground='#ffffff',command=gravarDados) # Cores, fontes, cor de fundo, cor da letra, função de salvar dados

but.place(x =210, y = 500, width=100, height=20) 

pg.mainloop() # Comando para iniciar o programa