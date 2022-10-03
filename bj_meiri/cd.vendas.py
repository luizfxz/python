from PyQt5 import uic, QtWidgets
import mysql
import mysql.connector

connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bijusmeiri'
    )

def cadastro_vendasd():
    
    linha1 = tela_vendas.cod_vendas.text()

    linha2 = tela_vendas.senha.text()

    linha3 = tela_vendas.nasc.text()

    linha4 = tela_vendas.cpf.text()

    linha5 = tela_vendas.cep.text()



    inserir = "INSERT INTO cd_user (id ,nome ,senha , nasc ,cpf ,cep ,endereco ,telefone ,email) values (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    dados = (linha1, linha2, linha3, linha4, linha5)

    cursor = connect.cursor()

    cursor.execute(inserir, dados)
  
    connect.commit()

    QtWidgets.QMessageBox.about(tela_vendas, 'Sucesso!', 'Cadastro feito com sucesso!')
    
    cursor.close()




app=QtWidgets.QApplication([])

tela_vendas=uic.loadUi('tela_venda.ui') # Inicializador da tela de cadastro de vendas

tela_vendas.show()

app.exec()