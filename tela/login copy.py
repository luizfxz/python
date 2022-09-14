import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '202173',
        database = 'bijusmeiri'
    )

    consulta_sql = "select id, nome, senha from login"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os autores cadastrados")
    for linha in linhas:
        print("Nome:", linha[0])
        print("Nome:", linha[1])
        print("Senha", linha[2], "\n")
except Error as e:
    print("Erro ao acessar tabela MySQL", e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")
