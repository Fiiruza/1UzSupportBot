import sqlite3
import config

class User:
    def __init__(self, first_name='', last_name='', phone_number='', user_id=0, username='', language=''):
        self.connection = sqlite3.connect(config.database_file_name)
        self.query = self.connection.cursor()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id
        self.username = username
        self.language = language

    @staticmethod
    def findUser(user_id):
        sql = "SELECT * FROM users WHERE user_id={0}".format(user_id)
        user = self.query.execute(sql)
        print(user)

    def save(self):
        pass

    