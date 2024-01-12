#!/usr/bin/python3

""" Python Script that lists all states from the db hbtn_0e_0usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Open connection
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()

    # Execut:Wing query
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
