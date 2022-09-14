from PyQt5 import uic, QtWidgets

# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_cadastro(): 
       cadastro.show()
       login.hide()

# Função para mostrar a tela de catalogo e esconder a tela de cadastro 

def chama_catalogo():
       catalogo.show()
       cadastro.hide()

# Função para mostrar a tela de compras e mostrar a tela de catalogo

def finaliza_compra():
       compras.show()
       catalogo.hide()

def tela_vendas ():



app = QtWidgets.QApplication([])
login = uic.loadUi('login.ui') # Tela de login
cadastro = uic.loadUi('cadastro.ui') # Tela de cadastro 
catalogo = uic.loadUi('catalogo.ui') # Tela de catalogo
compras = uic.loadUi('compras.ui') # Tela de compras

login.pushButton_2.clicked.connect(chama_cadastro) # Botão "registrar-se" que tem conexão com a função (chama_cadastro)
login.botao_entra.clicked.connect(chama_catalogo) # Botão "Entrar" que tem conexão com a função (chama_catalogo)
catalogo.carrinho.clicked.connect(finaliza_compra) # Botão "Carrinho" que tem conexão com a função (finalizar_compra)


       
login.show()
app.exec()






