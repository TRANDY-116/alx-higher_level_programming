#!/usr/bin/python3
"""
Script that lists all states with a name starting N(/Upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    # Add cursor
    cur = db.cursor()

    # Execute a query
    cur.execute("SELECT * FROM states WHERE name LIKE\
            BINARY 'N%' ORDER BY states.id ASC")

    # Fetch all the data from the query
    statesN = cur.fetchall()

    # Print all rows from the fetched data
    for states in statesN:
        print(states)

    # Close cursor
    cur.close()

    # Close Database
    db.close()
