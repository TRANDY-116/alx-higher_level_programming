#!/usr/bin/python3
"""
Script that takes in an arguemnt and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
but safe from MySQL injections!
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
                         passwd=password, db=name)

    # It gives us the ability to have multiple separate working environments
    # Via the same connection to the db

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ", [argv[4]])

    states = cur.fetchall()
    for state in states:
        print(state)

    # Clean up process
    cur.close()
    db.close()
