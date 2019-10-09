import psycopg2
import sqlite3

dbname = "rgfajssc"
username = "rgfajssc"
pass_word = "U0W4kG-Um-Pug_wj8ec9OnbkQ70deuZR"
host = "john.db.elephantsql.com"

pg_connect = psycopg2.connect(dbname=dbname, user=username,
                                password=pass_word, host=host)
cur = pg_connect.cursor()
#Query for Survived people by class
query = 'SELECT COUNT("Pclass") FROM titanic WHERE "Survived"=1 GROUP BY "Pclass";'
try:
    cur.execute(query)
    for row in cur:
        print(row[0])
except :
    pass

cur.close()
pg_connect.close()