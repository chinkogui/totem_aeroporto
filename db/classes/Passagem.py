import db.connectDatabase as db
import mysql.connector
from mysql.connector import errorcode


class Passagem:
    def __init__(self, cpf, numeroVoo, localizador, classe, preco):
        self.cpf = cpf
        self.numeroVoo = numeroVoo
        self.localizador = localizador
        self.classe = classe
        self.preco = preco

    def insertPassagem(self):
        sql = "INSERT INTO passagens (cpf, numeroVoo, localizador, classe, preco) " \
              "VALUES (%s, %s, %s, %s, %s);"
        val = (self.cpf, self.numeroVoo, self.localizador, self.classe, self.preco)
        try:
            connection = db.connect(False)
            connection["cursor"].execute(sql, val)
            connection["connection"].commit()
            passagemId = connection["cursor"].lastrowid
            db.closeConnect(connection)
            return passagemId
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                return 0
