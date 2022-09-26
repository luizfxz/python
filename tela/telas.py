from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector


connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bijusmeiri'
    )


# Função para mostrar a tela de cadastro e esconder a tela de login

def tela_login(): 
    
    global nomel

    nomel = loginkkk.caixa_login.text()

    senhap = loginkkk.caixa_senha.text()

    fotocata.nome.setText(nomel)

    cursor = connect.cursor()

    cursor.execute("SELECT nome, senha FROM login WHERE nome = '{}' and senha  = '{}'".format(nomel, senhap))

    for (nome, senha) in cursor:

        if nomel == nome or senhap == senha:

            QtWidgets.QMessageBox.about(loginkkk, 'Bijus Meiri', 'Seja bem vindo!')

            loginkkk.hide()

            telavendas.show()
            

        elif nomel != nome or senhap != senha:

            QtWidgets.QMessageBox.about(loginkkk, 'Bijus Meiri', 'Seja bem vindo!')
            
            loginkkk.caixa_login.setText('')

            loginkkk.caixa_senha.setText('')
            

        

def tela_cd_registro():

    nomel = cadastronew.c_nome.text()

    emaill = cadastronew.c_email.text()

    senhal = cadastronew.c_senha.text()

    cepl = cadastronew.c_cep.text()

    telefonel= cadastronew.c_telef.text()

    enderecol = cadastronew.c_endereco.text()

    nascl = cadastronew.c_nasc.text()

    cpfl = cadastronew.c_cpf.text()

    
    inserir_d = ("INSERT INTO cadastro (id, nome, email, senha, cep, telefone, endereco, nasc, cpf) values (null, %s, %s, %s, %s, %s, %s, %s, %s)")
    campos = (nomel, emaill, senhal, cepl, telefonel, enderecol, nascl, cpfl)

    cursor = connect.cursor()
    cursor.execute(inserir_d, campos)
    connect.commit()

def cd_vendas():

    nome_clientv = cadastrovenda.nome_client.text()

    telefonev = cadastrovenda.tel.text()

    cpfv = cadastrovenda.cpf.text()

    form_pagv = cadastrovenda.pagm.currentText()

    trocov = cadastrovenda.troco.text()

    codigo_prodv = cadastrovenda.codprodut.text()

    quantv = cadastrovenda.quant.text()

    marcav = cadastrovenda.marca.text()

    tamanhov = cadastrovenda.tamanho.currentText()

    precov = cadastrovenda.preco.text()

    inserir_vendas = ("INSERT INTO cd_vendas (nome_cliente, telefone, cpf, form_pag, troco, cod_prodt, quant, marca, tamanho, preco) values (%s, %s, %s, %s, %s, %s, %s,%s, %s,%s)")
    campos_vendas = (nome_clientv, telefonev, cpfv, form_pagv, trocov, codigo_prodv, quantv, marcav, tamanhov, precov)

    cursor = connect.cursor()

    cursor.execute(inserir_vendas, campos_vendas)

    connect.commit()

def tela_cadastro():
    cadastronew.show()

def alteracao(): 
    
    alter_meiri.show()
    

    cursor = connect.cursor()
    sql = "Select * from cadastro"
    cursor.execute(sql)

    leitura_sql = cursor.fetchall()

    alter_meiri.tableWidget.setRowCount(len(leitura_sql)) #tabela de clientes
    alter_meiri.tableWidget.setColumnCount(9) # colunas preenchidas na lista de cliente

    for i in range(0, len(leitura_sql)):
        for j in range(0, 9):
            alter_meiri.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_sql[i][j]))) # preenchimento das linhas e colunas

def excluir_dados(): 

    linha =  alter_meiri.tableWidget.currentRow() # linha selecionada
    alter_meiri.tableWidget.removeRow(linha) # remoção da linha

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id = " + str(valor_id))

    connect.commit()

    cursor.close()

    alter_meiri.hide()
    alter_meiri.show()


def edicao_dados(): 

    telavendas.hide()

    linha =  alter_meiri.tableWidget.currentRow()
    

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("SELECT * FROM cadastro WHERE id = " + str(valor_id))
    editar = cursor.fetchall()
    edit_meiri.show()

    

    edit_meiri.edit_cod.setText(str(editar[0][0]))
    edit_meiri.edit_nome.setText(str(editar[0][1]))
    edit_meiri.edit_email.setText(str(editar[0][2]))
    edit_meiri.edit_senha.setText(str(editar[0][3]))
    edit_meiri.edit_cep.setText(str(editar[0][4]))
    edit_meiri.edit_tele.setText(str(editar[0][5]))
    edit_meiri.edit_ende.setText(str(editar[0][6]))
    edit_meiri.edit_nasc.setText(str(editar[0][7]))
    edit_meiri.edit_cpf.setText(str(editar[0][8]))


def salvar_dados_editados():


    codl = edit_meiri.edit_cod.text()
    nomel = edit_meiri.edit_nome.text()
    emaill = edit_meiri.edit_email.text()
    senhal = edit_meiri.edit_senha.text()
    cepl = edit_meiri.edit_cep.text()
    telefonel = edit_meiri.edit_tele.text()
    enderecol = edit_meiri.edit_ende.text()
    nascl = edit_meiri.edit_nasc.text()
    cpfl = edit_meiri.edit_cpf.text()

    cursor = connect.cursor()
   
    atualizar ="UPDATE cadastro SET nome = '{}', email = '{}', senha = '{}', cep = '{}', telefone = '{}', endereco = '{}', nasc = '{}', cpf = '{}' where id = '{}' ".format (nomel,emaill,senhal,cepl, telefonel, enderecol, nascl, cpfl, codl)
    cursor.execute(atualizar)

    QtWidgets.QMessageBox.about(edit_meiri, 'Sucesso', 'Atualização feito com sucesso!')

    connect.commit()
    
    alter_meiri.close()
    edit_meiri.close()
    telavendas.show()

def botao_catalogo_admin():
    telavendas.hide()
    fotocata.show()

def cadastro_c():
    cadastronew.hide()
    loginkkk.show()

def tela_cadastro():
    loginkkk.hide()
    cadastronew.show()

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
    cadastronew.show()
    telavendas.hide()

# Função para esconder a tela de cadastro de cliente para a tela de vendas

def voltar_telas_vendas():
    cadastronew.hide()
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

alter_meiri=uic.loadUi('alter_meiri.ui')

edit_meiri=uic.loadUi('edit_meiri.ui')

client=uic.loadUi('client.ui') # Inicializador da tela de cadastro de cliente




loginkkk.login_entrar.clicked.connect(tela_login) # Botão de entrar da tela de login

loginkkk.login_registrar.clicked.connect(tela_cadastro)

cadastronew.c_inscrever.clicked.connect(tela_cd_registro) # Botão de inscrever-se da tela de login

cadastronew.c_inscrever.clicked.connect(cadastro_c) # Cadastro concluído

cadastronew.c_voltar.clicked.connect(cadastro_c) # botão de voltar

telavendas.vendas_admin.clicked.connect(chama_quinta_tela) # Botão de 'cadastro de vendas' da tela de escolha para o cadastro de vendas

telavendas.prod_admin.clicked.connect(chama_sexta_tela) # Botão de 'cadastro de produtos' da tela de escolha para o cadastro de produtos

telavendas.catalogo_admin.clicked.connect(botao_catalogo_admin) 

telavendas.alte_admin.clicked.connect(alteracao) 

telavendas.voltar.clicked.connect(volta_tela_login) # Botão 'voltar' da tela de escolha para a tela de login

cadastroprodt.voltar.clicked.connect(volta_tela_vendas) # Botão de 'voltar' da tela de cadastro de produtos para a tela de escolha

cadastrovenda.voltar.clicked.connect(volta_tela) # Botão de 'voltar' da tela de cadastro de vendas para a tela de escolha

cadastrovenda.salvarvendas.clicked.connect(cd_vendas)

fotocata.carro.clicked.connect(tela_pagamento) # Botão do carrinho para tela de pagamento

pagamentos.voltar.clicked.connect(voltar_catalogo) # Botão 'voltar' da tela de pagamento para o catalogo

telavendas.forne_admin.clicked.connect(chama_setima_tela) # Botão 'cadastro de fornecedores'  na tela de escolha para a tela de fornecedores
 
telavendas.cliente_admin.clicked.connect(chama_oitava) # Botão de 'cadastro de cliente' na tela de escolha para a tela de cadastro de clientes

client.voltar_cliente.clicked.connect(voltar_telas_vendas) # Botão de 'voltar' na tela de cadastro de cliente para a tela de cadastro de escolha

fornecedor.voltar_forn.clicked.connect(voltar_forn) # Botão de 'voltar' na tela de cadastro de fornecedores para a tela de cadastro de escolha

alter_meiri.alter_excluir.clicked.connect(excluir_dados)

alter_meiri.alter_alterar.clicked.connect(edicao_dados)

edit_meiri.edit_salvar.clicked.connect(salvar_dados_editados)

loginkkk.show() # Tela inicial de login

app.exec() # Execução das janelas
