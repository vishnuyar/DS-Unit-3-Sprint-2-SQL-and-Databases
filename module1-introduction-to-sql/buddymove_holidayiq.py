import pandas as pd
import sqlite3
#Import buddymove dataset by reading csv
buddymove_df = pd.read_csv('buddymove_holidayiq.csv')
#Printing the shape of the dataset and first five rows
print(buddymove_df.shape)
print(buddymove_df.head())
#Printing the number of null values in the dataset
print("The number of null values in the dataset are:\n",buddymove_df.isna().sum())

#Opening a sqlite connection and creating a database
database_name = 'buddymove_holidayiq.sqlite3'
conn = sqlite3.connect(database_name)
#Dumping the dataframe to the database
buddymove_df.to_sql('buddymove_tbl',con=conn,if_exists='replace')

#Checking for the first five rows to ensure the database dump was complete
query = 'SELECT * FROM buddymove_tbl LIMIT 5;'
#Query for number of rows in database
query_rows = 'SELECT COUNT("User Id") FROM buddymove_tbl;'
try:
    answer = conn.execute(query)
    for row in answer:
        print(row)
except:
    pass

#Getting the number of rows in the table
try:
    answer = conn.execute(query_rows)
    for row in answer:
        print(f'Number of rows in the table buddymove_tbl is :{row[0]}')
except:
    pass

#Number of users have rated atleast 100 in nature and atleast 100 in shopping category
query_users = 'SELECT COUNT("User Id") FROM buddymove_tbl WHERE\
                "Nature" >=100 AND "Shopping" >=100;'
try:
    answer = conn.execute(query_users)
    for row in answer:
        print(f'Number of users have rated atleast 100 in Nature and Shopping are :{row[0]}')
except:
    pass
#Query for getting average rating for all categories 
query_avg_rating = 'SELECT AVG("Sports"),AVG("Religious"),AVG("Nature"),AVG("Theatre"),AVG("Shopping"),AVG("Picnic") FROM buddymove_tbl;'
try:
    answer = conn.execute(query_avg_rating)
    for row in answer:
        print(f'Avg rating for Sports:{row[0]:.2f}')
        print(f'Avg rating for Religious:{row[1]:.2f}')
        print(f'Avg rating for Nature:{row[2]:.2f}')
        print(f'Avg rating for Theatre:{row[3]:.2f}')
        print(f'Avg rating for Shopping:{row[4]:.2f}')
        print(f'Avg rating for Picnic:{row[5]:.2f}')
except:
    pass
#committing the changes and closing the connection
conn.commit()
conn.close()
