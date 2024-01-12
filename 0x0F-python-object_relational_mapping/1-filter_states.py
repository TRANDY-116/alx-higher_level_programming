#!/usr/bin/python3

""" Python Script that lists all states from the db hbtn_0e_0usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    # Open connection to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()

    # Executing Query
    cur.execute("SELECT * FROM states WHERE name LIKE N%")

    # Fectching the result of the query
    rows = cur.fetchall()

    # Iterating through the rows to print each tuple
    for row in rows:
        print(row)

    #Closing The cursor and The database connection
    cur.close()
    db.close()
