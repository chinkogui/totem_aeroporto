import db.classes.Passagem as p

passagem = p.Passagem("27651967767", "2", "ABCD1234", "Economica", "270")
inserted = passagem.insertPassagem()
print(inserted)