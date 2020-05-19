avioesFk0 = "ALTER TABLE `avioes` ADD CONSTRAINT `avioes_fk0` FOREIGN KEY (`compAerea`) REFERENCES `compAerea`(`cnpj`);"

voosFk0 = "ALTER TABLE `voos` ADD CONSTRAINT `voos_fk0` FOREIGN KEY (`idAviao`) REFERENCES `avioes`(`id`);"

passagensFk0 = "ALTER TABLE `passagens` ADD CONSTRAINT `passagens_fk0` FOREIGN KEY (`cpf`) " \
               "REFERENCES `clientes`(`cpf`);"

passagensFk1 = "ALTER TABLE `passagens` ADD CONSTRAINT `passagens_fk1` FOREIGN KEY (`numeroVoo`) REFERENCES " \
               "`voos`(`numeroVoo`);"

checkinsFk0 = "ALTER TABLE `checkins` ADD CONSTRAINT `checkins_fk0` FOREIGN KEY (`passagem`) REFERENCES " \
              "`passagens`(`id`);"

checkinsFk1 = "ALTER TABLE `checkins` ADD CONSTRAINT `checkins_fk1` FOREIGN KEY (`pagamento`) REFERENCES " \
              "`pagamentos`(`id`);"

despachosFk0 = "ALTER TABLE `despachos` ADD CONSTRAINT `despachos_fk0` FOREIGN KEY (`passagem`) REFERENCES " \
               "`passagens`(`id`);"

despachosFk1 = "ALTER TABLE `despachos` ADD CONSTRAINT `despachos_fk1` FOREIGN KEY (`pagamento`) REFERENCES " \
               "`pagamentos`(`id`);"

def getAlterTables():
    return [
        avioesFk0,
        voosFk0,
        passagensFk0,
        passagensFk1,
        checkinsFk0,
        checkinsFk1,
        despachosFk0,
        despachosFk1
    ]
