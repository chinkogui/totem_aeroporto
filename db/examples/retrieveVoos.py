from db.controllers.controller import *

passagens = retrieveVoosByDataOrigemDestino("2020-07-24", "São Paulo", "Natal")
for passagem in passagens:
    print("Numero do Voo: {}".format(passagem["numeroVoo"]))
    print("Origem: {}".format(passagem["origem"]))
    print("Destino: {}".format(passagem["destino"]))
    print("Data: {}".format(passagem["data"]))
    print("Horario: {}".format(passagem["horario"]))
    print("Id do Avião: {}".format(passagem["idAviao"]))
    print("Portão de Embarque: {}".format(passagem["portaoEmbarque"]))
    print("----------------------------------------------------------------")

passagens = retrieveVoosByDataOrigemDestino("2020-07-24", "São Paulo", "Rio Grande do Sul")
for passagem in passagens:
    print("Numero do Voo: {}".format(passagem["numeroVoo"]))
    print("Origem: {}".format(passagem["origem"]))
    print("Destino: {}".format(passagem["destino"]))
    print("Data: {}".format(passagem["data"]))
    print("Horario: {}".format(passagem["horario"]))
    print("Id do Avião: {}".format(passagem["idAviao"]))
    print("Portão de Embarque: {}".format(passagem["portaoEmbarque"]))
    print("----------------------------------------------------------------")