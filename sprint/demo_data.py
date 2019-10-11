import sqlite3

""" Demo Data Query Using Sqlite 3 """

def data_operations(conn,query):
    """ Function which performs database operations and returns results """
    try:
        #creating a cursor for connection
        cursor = conn.cursor()
        #executing the query on the database and get the results
        results = cursor.execute(query).fetchall()
    except:
        return "error in data operations"
    
    #If No error is enountered, cursor is closed
    cursor.close()
    #Committing the data operatios
    conn.commit()
    #On successful completion return the results
    return results



def count_query(connect):
    """ 
    Function to find the number of rows in the demo table
    Expected Output :The number of rows in demo table is 6 
    
    """
    #How many rows in the demo table
    count_query = """SELECT COUNT(*) FROM demo; """
    #checking for 3 rows
    result = data_operations(connect,count_query)
    for row in result:
        print(f'The number of rows in demo table is {row[0]}')

def xy_query(connect):
    """ 
    Function for finding the number of rows where x and y are atleast equal to 5
    Expected Output :The number of rows where x and y is atleast 5: 4 
    
    """
    #How many rows where x and y are atleast 5
    xy_query = """ SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5; """
    #checking for atleast x y having value 5
    result = data_operations(connect,xy_query)
    for row in result:
        print(f'The number of rows where x and y is atleast 5: {row[0]}')


def y_unique(connect):
    """ 
    Function for finding the Number of Unique values of Y
    Expected output : The number of distinct values of y : 2 
    
    """
    #Query for unique values of y
    y_unique = """ SELECT COUNT(DISTINCT y) FROM demo ; """
    #checking for distinct values of y
    result = data_operations(connect,y_unique)
    for row in result:
        print(f'The number of distinct values of y : {row[0]}')
    

#Create a connection within a try excecpt block to pass errors without causing exception
try:
    #Creating a database with name demo_data
    connect = sqlite3.connect('demo_data.sqlite3')
    #SQL Query for creating the table
    create_table_query = """CREATE TABLE "demo" (
                            "s" TEXT,
                            "x" INTEGER,
                            "y" INTEGER
                            );  """
    
    #Creating the table by sending to data operations function
    result = data_operations(connect,create_table_query)
    
    #Inserting values into the demo table
    insert_query = """INSERT INTO demo (s,x,y) values
                                ("\'g\'",3,9),
                                ("\'v\'",5,7),
                                ("\'f\'",8,7) ;"""

    #inserting the values into the demo table
    data_operations(connect,insert_query)

    #Now checking the demo table for data
    count_query(connect) # Number of rows in the table
    xy_query(connect)  # Number of rows with x y values more than 5
    y_unique(connect)  # Number of distinct y values in the table
    
except:
    pass

#closing the connection to the database
connect.close()