#!/usr/bin/python3
" Script that lists all states from the database hbtn_0e_0_usa"
import MySQLdb
import sys

# Code should not be executed when imported
if __name__ == '__main__':

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQL.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    states =cur.fetchall()

    for state in states:
        print(states)

    cur.close()
    db.close()
