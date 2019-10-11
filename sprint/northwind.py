import sqlite3

"""Database operations for the NorthWind data """

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

#Creating a try catch block to safely operation on database
try:
    #Creating a connection to the Northwind database
    connect = sqlite3.connect('northwind_small.sqlite3')

    #query for ten most expensive items in the database
    expensive_query = """ SELECT ProductName, UnitPrice 
                            FROM Product 
                            ORDER BY UnitPrice DESC LIMIT 10 """
    result = data_operations(connect,expensive_query)
    print("The 10 Most expensive Items in the database are:\n")
    for row in result:
        print(f'{row[0]} : {row[1]}')
    #Query for the Avg age of the employee at the time of hiring
    avg_age_employee = """ SELECT AVG(HireDate - BirthDate) FROM Employee; """
    result = data_operations(connect,avg_age_employee)
    print("\n")
    for row in result:
        print(f'The Averag age of the employee is:{row[0]:0.2f}')
    #Query for avg age of the employee by city
    avg_employee_age_bycity = """ SELECT city, AVG(HireDate - BirthDate)
                                  FROM Employee GROUP BY City; """
    result = data_operations(connect,avg_employee_age_bycity)
    print("\nThe Averag age of the employee by City is :")
    for row in result:
        print(f'{row[0]} : {row[1]}')
    #Query for Top 10 expensive items along with Suppliet names
    expensive_query_supplier = """ SELECT CompanyName,ProductName, UnitPrice 
                            FROM Product, Supplier 
                            WHERE Supplier.Id = Product.SupplierId 
                            ORDER BY UnitPrice DESC LIMIT 10"""
    result = data_operations(connect,expensive_query_supplier)
    print("\nThe 10 Most expensive Items in the database with Supplier Names are:\n")
    for row in result:
        print(f'{row[0]} : {row[1]}: {row[2]}')
    #Query for the name of category with largest number of unique products
    largest_category = """ SELECT CategoryName FROM Category WHERE id = (
                            SELECT CategoryId FROM Product 
                            GROUP BY	CategoryId 
                            ORDER BY COUNT(CategoryId) DESC LIMIT 1) """
    result = data_operations(connect,largest_category)
    print("\n")
    for row in result:
        print(f'The Category with largest unique products is :{row[0]}')
    #Query for name of the Employee who has the most territories
    most_territories_employee = """ SELECT FirstName,LastName FROM Employee WHERE id = (
                                    SELECT EmployeeId FROM EmployeeTerritory 
                                    GROUP BY EmployeeId 
                                    ORDER BY COUNT(TerritoryId) DESC LIMIT 1
                                    ) """
    result = data_operations(connect,most_territories_employee)
    print("\n")
    for row in result:
        print(f'The Employee with most territories is  :{row[0]} {row[1]}')

except :
    pass
#closing the connection to the database
connect.close()