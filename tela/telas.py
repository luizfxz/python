from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector


connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bijusmeiri'
    )


'''def salvar_dados():
    


    linha1 = input(cadastronew.nome.text())

    linha2 = input(cadastronew.email.text())

    linha3 = input(cadastronew.senha.text())

    linha4 = input(cadastronew.cep.text())

    linha5 = input(cadastronew.telefone.text())

    linha6 = input(cadastronew.endereco.text())

    linha7 = input(cadastronew.nasc.text())

    linha8 = input(cadastronew.cpf.text())


    cursor = connect.cursor()

    inserir = """ INSERT INTO fornecedor (id, nome, email, senha, cep, telefone, endereco, nasc, cpf) values (null, %s,%s,%s,%s,%s, %s, %s, %s)"""
    
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7), str(linha8))

    cursor.execute(inserir, dados)

    connect.commit()
    
    print('Cadastro concluído!')

    cursor.close()
    print('Conexão encerrada!')'''

def logar():
    
    global login

    login = loginkkk.login.text()

    senha = loginkkk.senha.text()

    cursor = connect.cursor()
    
    consulta = ("select nome, senha from login where nome  = '{}' and senha = '{}'".format(login, senha))

    cursor.execute (consulta)

    senhabd = cursor.fetchall()

    if senha == senhabd[0][0]:
        loginkkk.close()
        cadastronew.show()

    else:
        print('Dados incorretos!')

# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_segunda_tela(): 
    cadastronew.show()
    loginkkk.hide()
   
# Função para mostrar a tela de catalogo e esconder a tela de cadastro

def chama_terceira_tela():
    fotocata.show()
    cadastronew.hide()

# Função para mostrar a tela de escolha e esconder a tela de login

def chama_quarta_tela():
    telavendas.show()
    loginkkk.hide()
   
# Função para mostrar a tela de cadastro de vendas e esconder a tela de vendas

def chama_quinta_tela():
    cadastrovenda.show()
    telavendas.hide()
   
# Função para mostrar a tela de cadastro de produto e esconder a tela de vendas

def chama_sexta_tela():
    cadastroprodt.show()
    telavendas.hide()

# Função para esconder a tela de escolha e mostrar a tela de login

def volta_tela_login():
    telavendas.hide()
    loginkkk.show()

# Função para esconder a tela de cadastro de produtos e mostrar a tela de escolha

def volta_tela_vendas():
    cadastroprodt.hide()
    telavendas.show()

# Função para esconder a tela de cadastro de venda e mostrar a tela de escolha

def volta_tela():
    cadastrovenda.hide()
    telavendas.show()
   
# Função para mostrar a tela de pagamento e esconder a tela de catalogo

def tela_pagamento():
    pagamentos.show()
    fotocata.hide()

# Função para esconder a tela de pagamentos e mostrar a tela de  catalogo

def voltar_catalogo():
    pagamentos.hide
    fotocata.show()
   
# Função para mostrar a tela de cadastro de fornecedor e esconder a tela de escolha

def chama_setima_tela():
    fornecedor.show()
    telavendas.hide()

# Função para mostrar a tela de clientes e esconder a tela de escolha

def chama_oitava():
    client.show()
    telavendas.hide()

# Função para esconder a tela de cadastro de cliente para a tela de vendas

def voltar_telas_vendas():
    client.hide()
    telavendas.show()

def voltar_forn():
    fornecedor.hide()
    telavendas.show()


app=QtWidgets.QApplication([])

loginkkk=uic.loadUi('loginkkk.ui') # Inicializador da tela de login

cadastronew=uic.loadUi('cadastronew.ui') # Inicializador da tela de cadastro

fotocata=uic.loadUi('fotocata.ui') # Inicializador da tela de catálogo

telavendas=uic.loadUi('telavendas.ui') # Inicializador da tela de escolhas

cadastrovenda=uic.loadUi('cadastrovenda.ui') # Inicializador da tela de cadastro de vendas

cadastroprodt=uic.loadUi('cadastro-prodt.ui') # Inicializador da tela de cadastro de produtos

pagamentos=uic.loadUi('pagamentos.ui') # Inicializador da tela de pagamento

fornecedor=uic.loadUi('fornecedor.ui') # Inicializador da tela de cadastro de fornecedor

client=uic.loadUi('client.ui') # Inicializador da tela de cadastro de cliente


loginkkk.kkk.clicked.connect(chama_segunda_tela) # Botão de entrar da tela de login


cadastronew.incresverse.clicked.connect(chama_terceira_tela) # Botão de inscrever-se da tela de login

# loginkkk.entrar.clicked.connect(chama_quarta_tela) # Botão de entrar da tela de login para tela de escolha

telavendas.vendas.clicked.connect(chama_quinta_tela) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

telavendas.prod.clicked.connect(chama_sexta_tela) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

telavendas.voltar.clicked.connect(volta_tela_login) # Botão 'voltar' da tela de escolha para a tela de login

cadastroprodt.voltar.clicked.connect(volta_tela_vendas) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cadastrovenda.voltar.clicked.connect(volta_tela) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

fotocata.carro.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

pagamentos.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

telavendas.forne.clicked.connect(chama_setima_tela) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
telavendas.cliente.clicked.connect(chama_oitava) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

client.voltar_cliente.clicked.connect(voltar_telas_vendas) # Botão de 'voltar' na tela de cadastro de cliente para a tela de cadastro de escolha

fornecedor.voltar_forn.clicked.connect(voltar_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

loginkkk.show() # Tela inicial de login

app.exec() # Execução das janelas