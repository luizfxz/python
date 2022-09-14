from PyQt5 import uic, QtWidgets # Import do Pyqt5
import mysql.connector # importando o mysql.conncetor
from mysql.connector import Error #importando o Error

connect = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bijusmeiri'
    ) # conectar ao banco de dados


def logar(): #evento

    login = loginkkk.login.text() # localização do campo de digitar o login /usuário

    senha = loginkkk.senha.text() # localização do campo de digitar a senha do

    cursor = connect.cursor()
    
    consulta_sql = """ select nome,senha from login """

    cursor.execute(consulta_sql)

    linhas = cursor.fetchall()

    for linha in linhas:
        if linha[0] == login and linha[1] == senha:
            print('Erroaaaa')
            #telavendas.show()
        else:
            print('Erro')
    

app=QtWidgets.QApplication([])

loginkkk=uic.loadUi('loginkkk.ui') # Inicializador da tela de login
telavendas=uic.loadUi('telavendas.ui')

loginkkk.show() # Tela inicial de login

app.exec()