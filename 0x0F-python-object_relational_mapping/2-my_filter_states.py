#!/usr/bin/python3
"""
Script that takes in an argument and and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys

# The code that should be executed ehrn imported
if __name__ == '__main__':

    # Arguments
    username = argv[1]
    password = argv[2]
    name = argv[3]
    state_name = argv[4]

    # connecting to a database
    db = MySQLdb.connect(host=username, port=3306, user=username,
                         passwd=password, db=name)

    # Cursor addition
    cur = db.cursor()
    cur.excute("SELECT * FROM states WHERE name Like '{}'".format(state_name))

    state_value = cur.fetchall()
    for value in state_value:
        print(value)

    cur.close()
    db.close()
