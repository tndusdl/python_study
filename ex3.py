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


cursor.execute('SELECT * FROM city ORDER BY population DESC LIMIT 4;')
results = cursor.fetchall()
for row in results:
    print(row)   
    
    

df = pd.DataFrame(results)
print(df.head(10), end="\n\n")

conn.close()