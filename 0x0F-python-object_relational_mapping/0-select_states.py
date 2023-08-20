#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

# Code should not be executed when imported
if __name__ == '__main__':
    # Connection TO THE MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    # Create cursor object to in interact with db
    cur = db.cursor()

    # Execute a query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the data from the Query
    states = cur.fetchall()

    # Print each row of the Fetched data
    for state in states:
        print(state)

    # Close cursor
    cur.close()

    # Close Database
    db.close()
