import mysql.connector
from mysql.connector import errorcode

credential = {
    'hostname': 'localhost',
    'username': 'root',
    'password': '',
    'database': 'airport'
}


def connect(isCreate=False):
    try:
        if isCreate:
            connection = mysql.connector.connect(host=credential["hostname"], user=credential["username"],
                                                 password=credential["password"])
        else:
            connection = mysql.connector.connect(host=credential["hostname"], user=credential["username"],
                                                 password=credential["password"], database=credential["database"])

        cnx = {
            "connection": connection,
            "cursor": connection.cursor()
        }
        return cnx

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Há algo de errado com seu usuário ou senha!")
        elif err.errno == errorcode.CR_CONNECTION_ERROR:
            print("Ocorreu um erro na conexão com o banco de dados! Tente novamente mais tarde.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
    else:
        connection.close()


def closeConnect(credentialAccess):
    credentialAccess["connection"].close
