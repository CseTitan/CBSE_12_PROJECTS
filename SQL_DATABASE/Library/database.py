# WAP to display the name and id of all the records in the ACCESSORIES table, using their feild names.


import mysql.connector

HOST = "localhost"
USER = "scott"
PASSWORD = "scotttiger"
DATABASE = "library"


def get_database():
    try:
        database = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = database.cursor(dictionary=True)
        return database, cursor
    except mysql.connector.Error:
        return None, None
