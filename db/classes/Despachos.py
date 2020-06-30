import db.connectDatabase as db
import mysql.connector
from mysql.connector import errorcode

class Checkin:
    def __init__(self, passagem, pagamento):
        self.passagem = passagem
        self.pagamento = pagamento

    def insertCheckin(self):
        sql = "INSERT INTO checkins (passagem, pagamento) VALUES (%s, %s)"
        val = (self.passagem, self.pagamento)
        try:
            connection = db.connect(False)
            connection["cursor"].execute(sql, val)
            connection["connection"].commit()
            db.closeConnect(connection)
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                return False
