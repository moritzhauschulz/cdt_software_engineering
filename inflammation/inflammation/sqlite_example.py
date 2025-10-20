# Original code: Function that performs a database query
import sqlite3

def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def query_database(sql, conn = None):
    # connection - a live communication channel between the app and the database
    if conn is None:
        raise TypeError("No database connection given.")
    # cursor - used to traverse and manipulate results returned by a query
    cursor = conn.cursor()
    # we pass a string named 'sql' that contains our SQL query
    cursor.execute(sql)
    # fetchall - returns a list of tuples containing all rows of our result
    result = cursor.fetchall()
    conn.close()
    return result

