import pymysql

hostname = 'localhost'
username = 'root'
password = ''
database = 'airport'


def connect():
    connection = pymysql.connect(host=hostname, username=username, passwd=password, database=database)
    return connection

