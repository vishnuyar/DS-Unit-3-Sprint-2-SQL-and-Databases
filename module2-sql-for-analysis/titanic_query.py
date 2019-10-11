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
query = 'SELECT survived,pclass, COUNT(pclass) FROM titanic  \
        GROUP BY (pclass,survived) order by survived asc ,pclass asc;'
try:
    cur.execute(query)
    for row in cur:
        print(row)
except :
    pass

cur.close()
pg_connect.close()