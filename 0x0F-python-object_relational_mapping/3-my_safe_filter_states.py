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
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    # Add cursor
    cur = db.cursor()

    # Execut Query
    cur.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ", (argv[4]))

    # Fetch Query Response
    states = cur.fetchall()
    for state in states:
        print(state)

    # Clean up process
    cur.close()
    db.close()
