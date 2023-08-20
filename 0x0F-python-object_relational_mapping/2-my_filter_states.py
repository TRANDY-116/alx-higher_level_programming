#!/usr/bin/python3
"""
Script that takes in an argument and and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

# The code that should be executed ehrn imported
if __name__ == '__main__':

    # connection to a database
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    # Cursor addition
    cur = db.cursor()
    cur.excute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC ".format(argv[4]))

    # Fetch query response
    state_value = cur.fetchall()

    # Print out each Row
    for value in state_value:
        print(value)

    # CLose Cursor and Database
    cur.close()
    db.close()
