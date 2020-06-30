import db.connectDatabase as db
import mysql.connector
from mysql.connector import errorcode


class Pagamento:
    def __init__(self, formaPagamento, parcelamento):
        self.formaPagamento = formaPagamento
        self.parcelamento = parcelamento

    def insertPagamento(self):
        sql = "INSERT INTO pagamentos (formaPagamento, parcelamento) " \
              "VALUES (%s, %s);"
        val = (self.formaPagamento, self.parcelamento)
        try:
            connection = db.connect(False)
            connection["cursor"].execute(sql, val)
            connection["connection"].commit()
            pagamentoId = connection["cursor"].lastrowid
            db.closeConnect(connection)
            return pagamentoId
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                return 0
