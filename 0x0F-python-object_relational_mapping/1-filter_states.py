#!/usr/bin/python3
"""
Script that lists all states with a name starting N(/Upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported

# Arguments
username = argv[1]
password = argv[2]
name = argv[3]
if __name__ == '__main__':
    db = MySQLdb.connect(host=username, port=3306, user=username,
                         password=password, db=name)

    # Add cursor
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE\
            BINARY 'N%' ORDER BY states.id ASC")

    statesN = cur.fetchall()
    for states in statesN:
        print(states)

    cur.close()
    db.close()
