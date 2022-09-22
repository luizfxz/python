from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql
import mysql.connector

numero_id = 0

connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '149844Sqs#',
        database = 'tb_cadastro'
    )


def registro():

    nomel = cd_cliente.cd_nome.text()

    emaill = cd_cliente.cd_email.text()

    senhal = cd_cliente.cd_senha.text()

    cepl = cd_cliente.cd_cep.text()

    telefonel= cd_cliente.cd_telefone.text()

    enderecol = cd_cliente.cd_endereco.text()

    nascl = cd_cliente.cd_nasc.text()

    cpfl = cd_cliente.cd_cpf.text()

    
    inserir_d = ("INSERT INTO cadastro (id, nome, email, senha, cep, telefone, endereco, nasc, cpf) values (null, %s, %s, %s, %s, %s, %s, %s, %s)")
    campos = (nomel, emaill, senhal, cepl, telefonel, enderecol, nascl, cpfl)

    cursor = connect.cursor()
    cursor.execute(inserir_d, campos)
    connect.commit()


def tela_cadastro():
    cd_cliente.show()

def alteracao(): 
    
    alter_meiri.show()
    tela_login.hide()

    cursor = connect.cursor()
    sql = "Select * from cadastro"
    cursor.execute(sql)

    leitura_sql = cursor.fetchall()

    alter_meiri.tableWidget.setRowCount(len(leitura_sql))
    alter_meiri.tableWidget.setColumnCount(9)

    for i in range(0, len(leitura_sql)):
        for j in range(0, 9):
            alter_meiri.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_sql[i][j])))

def excluir_dados(): 

    linha =  alter_meiri.tableWidget.currentRow()
    alter_meiri.tableWidget.removeRow(linha)

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id = " + str(valor_id))


def edicao_dados(): 
    global numero_id
    linha =  alter_meiri.tableWidget.currentRow()
    

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("SELECT * FROM cadastro WHERE id = " + str(valor_id))
    editar = cursor.fetchall()
    edit_meiri.show()

    numero_id = valor_id

    edit_meiri.edit_cod.setText(str(editar[0][0]))
    edit_meiri.edit_nome.setText(str(editar[0][1]))
    edit_meiri.edit_email.setText(str(editar[0][2]))
    edit_meiri.edit_senha.setText(str(editar[0][3]))
    edit_meiri.edit_cep.setText(str(editar[0][4]))
    edit_meiri.edit_tel.setText(str(editar[0][5]))
    edit_meiri.edit_ende.setText(str(editar[0][6]))
    edit_meiri.edit_nasc.setText(str(editar[0][7]))
    edit_meiri.edit_cpf.setText(str(editar[0][8]))

    print(editar[0])

def salvar_dados_editados():
    global numero_id
    print(numero_id)

    cod = edit_meiri.edit_cod.text()
    nome = edit_meiri.edit_nome.text()
    email = edit_meiri.edit_email.text()
    senha = edit_meiri.edit_senha.text()
    cep = edit_meiri.edit_cep.text()
    telefone = edit_meiri.edit_telefone.text()
    endereco = edit_meiri.edit_ende.text()
    nasc = edit_meiri.edit_nasc.text()
    cpf = edit_meiri.edit_cpf.text()

    cursor = connect.cursor()

    cursor.execute("UPDATE cadastro SET id = '{}', nome = '{}' , email = '{}' , senha = '{}' , cep = '{}' , telefone = '{}', endereco'{}', nasc = '{}', cpf = '{}' where id = {}".format(cod, nome, email, senha, cep, telefone, endereco, nasc, cpf))

    edit_meiri.close()
    edit_meiri.sho()
