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
    query = """
        SELECT cities.id, cities.name
        FROM states
        JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        
    cursor.execute(query, (argv[4],))
    
    # fetch all the data returned by the query
    data = my_cursor.fetchall()

    # fetched data and print each row
    for rows in data:
        print(rows)

    # Close cursor
    cur.close()

    # Close database
    db.close()
