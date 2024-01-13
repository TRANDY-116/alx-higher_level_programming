#!/usr/bin/python3

"""
Script that lsits a;; cities from a database
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

    query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states ON cities.state_id "
            "= states.id ORDER BY cities.id ASC;"
            )
    cur.execute(query)

    # Fectching the result of the query
    rows = cur.fetchall()

    # Iterating through the rows to print each tuple
    for row in rows:
        print(row)

    # Closing The cursor and The database connection
    cur.close()
    db.close()
