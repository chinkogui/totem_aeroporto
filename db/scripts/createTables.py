from db.models.mysqlTables import getTables
from db.models.mysqlAlterTables import getAlterTables
import db.connectDatabase as db

tables = getTables()
alterTables = getAlterTables()


def createTables(credential):
    for table in tables:
        credential["cursor"].execute("USE airport;")
        try:
            credential["cursor"].execute(table)
        except Exception as e:
            print(e)