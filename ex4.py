import pandas as pd
import mariadb

conn = mariadb.connect(
    user="user017",
    password="!ai123",
    host="edu.ithows.com",
    port=53306,
    database="edudb"
)
cursor = conn.cursor()

cursor.execute('INSERT INTO user017 (userId, userPassword) VALUES ("Song", "!ai123") ;')
# cursor.execute('DELETE FROM user017 WHERE userId = "Park";')
    
conn.commit()
conn.close()