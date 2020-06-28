import db.connectDatabase as db
import db.scripts.createTables as tables

try:
    credential = db.connect(True)
    credential["cursor"].execute("CREATE DATABASE airport;")
    print("Criando banco de dados! Aguarde!")
    credential["connection"].commit()

except:
    print("Banco já existe! Solicitando a criação das tabelas!")

finally:
    print("Executando de qualquer forma")
    tables.createTables(credential)
    db.closeConnect(credential)
