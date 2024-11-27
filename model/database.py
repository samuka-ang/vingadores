from json import load
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv
 
class Database:
    def __init__(self):
        load_dotenv() # carregando as variáveis de ambiente
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')
 
 
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.cursor = self.connection.cursor()
            print('Conexão com o banco de dados realizadas com sucesso')
        except Error as e:
            print(f'Erro: {e}')
 
#Database().connect()
db = Database()
db.connect()
db.disconnect()