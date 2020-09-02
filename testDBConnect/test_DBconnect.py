import mysql.connector
import ibm_db
from mysql.connector import Error

def test_dbConnect():
    connection = mysql.connector.connect(host='localhost',
                                         database='world',
                                         user='root',
                                         password='root')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("select * FROM city where Population > 7000000 limit 10")

        # Below Method will return the data form table in form of tuple
        cityName = cursor.fetchmany(10)
        for i in range(10):
            print(cityName[i])


