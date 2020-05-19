tabelaAvioesSql = """CREATE TABLE `avioes` (\
 `id` varchar(15) NOT NULL,\
 `modelo` varchar(20) NOT NULL,\
 `compAerea` INT(20) NOT NULL,\
 `lotacao` INT NOT NULL,\
 PRIMARY KEY (`id`)\
);"""

tabelaVoosSql = """CREATE TABLE `avioes` (\
 `id` varchar(15) NOT NULL,\
 `modelo` varchar(20) NOT NULL,\
 `compAerea` INT(20) NOT NULL,\
 `lotacao` INT NOT NULL,\
 PRIMARY KEY (`id`)\
);"""

tabelaClientesSql = """CREATE TABLE `clientes` (
 `cpf` varchar(11) NOT NULL,
 `rg` varchar(15) NOT NULL UNIQUE,
 `nome` varchar(20) NOT NULL,
 `sobrenome` varchar(50) NOT NULL,
 `dataNascimento` DATE NOT NULL,
 `estado` varchar(2) NOT NULL,
 `cidade` varchar(20) NOT NULL,
 `bairro` varchar(20) NOT NULL,
 `rua` varchar(20) NOT NULL,
 `numeroCasa` INT NOT NULL,
 `email` varchar(50) NOT NULL,
 `celular` varchar(11) NOT NULL,
 `telefone` varchar(11),
 PRIMARY KEY (`cpf`)
);"""

tabelaPassagensSql = """CREATE TABLE `passagens` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `cpf` varchar(11) NOT NULL,
 `numeroVoo` INT NOT NULL AUTO_INCREMENT,
 `localizador` varchar(15) NOT NULL UNIQUE,
 `classe` varchar(20) NOT NULL,
 `preco` FLOAT NOT NULL,
 PRIMARY KEY (`id`)
);"""

tabelaCheckinsSql = """CREATE TABLE `checkins` (
 `passagem` INT NOT NULL AUTO_INCREMENT,
 `pagamento` INT NOT NULL,
 PRIMARY KEY (`passagem`)
);"""

tabelaDespachosSql = """CREATE TABLE `despachos` (
 `passagem` INT NOT NULL AUTO_INCREMENT,
 `pagamento` INT NOT NULL,
 PRIMARY KEY (`passagem`)
);"""

tabelaPagamentosSql = """CREATE TABLE `pagamentos` (
 `id` INT NOT NULL AUTO_INCREMENT,
 `formaPagamento` varchar(20) NOT NULL,
 `parcelamento` INT,
 PRIMARY KEY (`id`)
);"""

tabelaCompAeareaSql = """CREATE TABLE `compAerea` (
 `cnpj` varchar(13) NOT NULL AUTO_INCREMENT,
 `nomeFantasia` varchar(50) NOT NULL AUTO_INCREMENT,
 `razaoSocial` varchar(50) NOT NULL AUTO_INCREMENT,
 PRIMARY KEY (`cnpj`)
);"""


def getTables():
    return [
        tabelaAvioesSql,
        tabelaVoosSql,
        tabelaClientesSql,
        tabelaPassagensSql,
        tabelaCheckinsSql,
        tabelaDespachosSql,
        tabelaPagamentosSql,
        tabelaCompAeareaSql
    ]
