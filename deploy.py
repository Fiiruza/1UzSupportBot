import sqlite3
import config

connection = sqlite3.connect(config.database_file_name)
query = connection.cursor()

#Table is used just for statistics and report
#it does remember what language speaks user for our bot
create_table = '''CREATE TABLE users (
    row_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR,
    user_id INTEGER,
    username VARCHAR,
    language VARCHAR,
)'''

query.execute(create_table)
connection.commit()
connection.close()