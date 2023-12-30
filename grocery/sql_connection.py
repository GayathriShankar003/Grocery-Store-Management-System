import mysql.connector

__mydb = None

def get_sql_connection():
    global __mydb
    if __mydb is None:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3663",
            database="grocery_store"
        )

    return mydb