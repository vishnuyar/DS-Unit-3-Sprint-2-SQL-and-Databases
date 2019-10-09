import psycopg2
from sqlalchemy import create_engine
import pandas as pd

#Reading titanic file to upload into pandas
titanic = pd.read_csv('titanic.csv')
#Print the shape of titanic and print the top 5 rows
print(titanic.shape)
print(titanic.head())
#Pring the columns of the titanics dataframe
print(titanic.columns)

from sqlalchemy import create_engine

dbname = "rgfajssc"
username = "rgfajssc"
pass_word = "SECRET"
host = "john.db.elephantsql.com"
#creating creating engine inserting the titanic dataframe to postgres
try:
    engine = create_engine(f'postgresql://{username}:{pass_word}@{host}/{username}')
    titanic.to_sql('titanic', engine)
except:
    pass

# pg_connect = psycopg2.connect(dbname=dbname, user=username,
#                                 password=pass_word, host=host)
# cur = pg_connect.cursor()