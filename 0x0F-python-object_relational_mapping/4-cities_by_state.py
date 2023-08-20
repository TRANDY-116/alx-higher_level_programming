#!/usr/bin/python3
"""
Module that connects a python Script to a database
"""
import MySQLdb
from sys import argv

if __name__ = '__main__':
    
    # Connection to the Database
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    # add Cursor
    cur = db.cursor()

    # Execution of Query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities 
                JOIN states ON states.id = cities.states_id
                ORDER BY cities.id")

    # fetch all the data returned by the query
    data = my_cursor.fetchall()

    # fetched data and print each row
    for rows in data:
        print(rows)

    # Close cursor
    cur.close()

    # Close database
    db.close()
