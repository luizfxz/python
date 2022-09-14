from PyQt5 import uic, QtWidgets

def chama_terceira():
       catalogo.show()

app = QtWidgets.QApplication([])
login = uic.loadUi('login.ui')
catalogo = uic.loadUi('catalogo.ui')
login.botao_entra.clicked.connect(chama_terceira)

login.show()
app.exec()

