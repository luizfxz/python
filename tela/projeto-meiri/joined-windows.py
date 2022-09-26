from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector


connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '149844Sqs#',
        database = 'tb_cadastro'
    )


# Função para mostrar a tela de cadastro e esconder a tela de login

def chama_segunda_tela(): 
    
    global nomel

    nomel = tela_login.login.text()

    senhap = tela_login.senha.text()

    cursor = connect.cursor()

    cursor.execute("SELECT nome, senha FROM login WHERE nome = '{}' and senha  = '{}'".format(nomel, senhap))

    for (nome, senha) in cursor:
        if nomel == nome or senhap == senha:

            tela_login.hide()
            tela_admin.show()
    else:
        #loginkkk.error.setText('Usuário ou senha inválida')
        print('Dados inválidos!')

def registro():

    nomel = cd_cliente.nome.text()

    emaill = cd_cliente.email.text()

    senhal = cd_cliente.senha.text()

    cepl = cd_cliente.cep.text()

    telefonel= cd_cliente.telefone.text()

    enderecol = cd_cliente.endereco.text()

    nascl = cd_cliente.nasc.text()

    cpfl = cd_cliente.cpf.text()

    
    inserir_d = ("INSERT INTO cadastro (id, nome, email, senha, cep, telefone, endereco, nasc, cpf) values (null, %s, %s, %s, %s, %s, %s, %s, %s)")
    campos = (nomel, emaill, senhal, cepl, telefonel, enderecol, nascl, cpfl)

    cursor = connect.cursor()
    cursor.execute(inserir_d, campos)
    connect.commit()

def tela_cadastro():
    tela_login.hide()
    cd_cliente.show()

# Função para mostrar a tela de catalogo e esconder a tela de cadastro

def chama_terceira_tela():
    tela_catalogo.show()
    cd_cliente.hide()

# Função para mostrar a tela de escolha e esconder a tela de login

def chama_quarta_tela():
    tela_admin.show()
    tela_login.hide()
   
# Função para mostrar a tela de cadastro de vendas e esconder a tela de vendas

def chama_quinta_tela():
    cd_vendas.show()
    tela_admin.hide()
   
# Função para mostrar a tela de cadastro de produto e esconder a tela de vendas

def chama_sexta_tela():
    cd_prodt.show()
    tela_admin.hide()

# Função para esconder a tela de escolha e mostrar a tela de login

def volta_tela_login():
    tela_admin.hide()
    tela_login.show()

# Função para esconder a tela de cadastro de produtos e mostrar a tela de escolha

def volta_tela_vendas():
    cd_prodt.hide()
    tela_admin.show()

# Função para esconder a tela de cadastro de venda e mostrar a tela de escolha

def volta_tela():
    cd_vendas.hide()
    tela_admin.show()
   
# Função para mostrar a tela de pagamento e esconder a tela de catalogo

def tela_pagamento():
    tela_pag.show()
    tela_catalogo.hide()

# Função para esconder a tela de pagamentos e mostrar a tela de  catalogo

def voltar_catalogo():
    tela_pag.hide
    tela_catalogo.show()
   
# Função para mostrar a tela de cadastro de fornecedor e esconder a tela de escolha

def chama_setima_tela():
    cd_forn.show()
    tela_admin.hide()

# Função para mostrar a tela de clientes e esconder a tela de escolha

def chama_oitava():
    cd_cliente.show()
    tela_admin.hide()

# Função para esconder a tela de cadastro de cliente para a tela de vendas

def voltar_telas_vendas():
    cd_cliente.hide()
    tela_admin.show()

def voltar_forn():
    cd_forn.hide()
    tela_admin.show()


app=QtWidgets.QApplication([])

tela_login=uic.loadUi('meiri-login.ui') # Inicializador da tela de login

cd_cliente=uic.loadUi('cd-cliente.ui') # Inicializador da tela de cadastro

tela_catalogo=uic.loadUi('meiri-cat.ui') # Inicializador da tela de catálogo

tela_admin=uic.loadUi('meiri-admin.ui') # Inicializador da tela de admin

cd_vendas =uic.loadUi('cd-vendas.ui') # Inicializador da tela de cadastro de vendas

cd_prodt = uic.loadUi('cd-prodt.ui') # Inicializador da tela de cadastro de produtos

tela_pag = uic.loadUi('meiri-pag.ui') # Inicializador da tela de pagamento

cd_forn = uic.loadUi('cd-forn.ui') # Inicializador da tela de cadastro de fornecedor

'''cd_cliente =uic.loadUi('cd-cliente.ui') Inicializador da tela de cadastro de cliente'''


tela_login.entrar.clicked.connect(chama_segunda_tela) # Botão de entrar da tela de login

tela_login.kkk.clicked.connect(tela_cadastro)

cd_cliente.incresverse.clicked.connect(registro) # Botão de inscrever-se da tela de login

#oginkkk.entrar.clicked.connect(chama_quarta_tela) # Botão de entrar da tela de login para tela de escolha

tela_admin.vendas.clicked.connect(chama_quinta_tela) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

tela_admin.prod.clicked.connect(chama_sexta_tela) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

tela_admin.voltar.clicked.connect(volta_tela_login) # Botão 'voltar' da tela de escolha para a tela de login

cd_prodt.voltar.clicked.connect(volta_tela_vendas) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cd_vendas.voltar.clicked.connect(volta_tela) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

tela_catalogo.carro.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

tela_pag.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

tela_admin.forne.clicked.connect(chama_setima_tela) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
cd_vendas.cliente.clicked.connect(chama_oitava) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

cliente_admin.voltar_cliente.clicked.connect(voltar_telas_vendas) # Botão de 'voltar' na tela de cadastro de cliente para a tela de cadastro de escolha

cd_forn.voltar_forn.clicked.connect(voltar_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

tela_login.show() # Tela inicial de login

app.exec() # Execução das janelas