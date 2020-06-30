import db.connectDatabase as db
import mysql.connector
from db.transformers.transformer import *


def retrievePassagemWithLocalizador(localizador):
    sql = "SELECT id FROM passagens WHERE localizador = %s"
    where = (localizador,)
    try:
        connection = db.connect(False)
        connection["cursor"].execute(sql, where)
        passagemId = transformPassagem(connection["cursor"].fetchone())
        db.closeConnect(connection)
        return passagemId
    except mysql.connector.Error as err:
        return 0


def isCheckinPendent(passagemId):
    sql = "SELECT COUNT(passagem) FROM checkins WHERE passagem = %s"
    where = (passagemId,)
    try:
        connection = db.connect(False)
        connection["cursor"].execute(sql, where)
        checkin = connection["cursor"].fetchone()
        print(checkin)
        db.closeConnect(connection)
        if checkin[0] > 0:
            return False
        return True
    except mysql.connector.Error as err:
        print(err)
        return 0

def isBagagemPendent(passagemId):
    sql = "SELECT COUNT(passagem) FROM despachos WHERE passagem = %s"
    where = (passagemId,)
    try:
        connection = db.connect(False)
        connection["cursor"].execute(sql, where)
        checkin = connection["cursor"].fetchone()
        print(checkin)
        db.closeConnect(connection)
        if checkin[0] > 0:
            return False
        return True
    except mysql.connector.Error as err:
        print(err)
        return 0

def retrieveVoosByDataOrigemDestino(data, origem, destino):
    sql = "SELECT * FROM voos WHERE data = %s AND origem = %s AND destino = %s"
    where = (data, origem, destino)
    try:
        connection = db.connect(False)
        connection["cursor"].execute(sql, where)
        voos = transformVoos(connection["cursor"].fetchall())
        db.closeConnect(connection)
        return voos
    except mysql.connector.Error as err:
        print(err)
        return 0