#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

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
    cur.execute(
            "SELECT * FROM states "
            "WHERE name = '{}' "
            "ORDER BY states.id ASC".format(argv[4])
            )

    # Fectching the result of the query
    rows = cur.fetchall()

    # Iterating through the rows to print each tuple
    for row in rows:
        print(row)

    # Closing The cursor and The database connection
    cur.close()
    db.close()
