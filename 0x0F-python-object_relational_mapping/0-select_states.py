#!/usr/bin/python3

""" ORM Function """

import MySQLdb
import sys

if __name__ == 'main':
	"""connects, queries, and displays results from a database"""
    # check arguments provided by user
    if len(sys.argv != 4):
        sys.exit(1)

        # assign arguments to variables
        user = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # connect to database
        try:
            db = MySQLdb.connect(
                host='localhost',
                user=username,
                password=password,
                database=database,
                port=3306)
            except MySQLdb.Error as e:
                print(f'Error connecting to database: {e}')
                sys.exit(2)

    # create a cursor object
    cursor = db.cursor

    # query database
    query = 'SELECT id, name FROM states ORDER BY states.id ASC'
    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f'Error Executing query: {e}')
        sys.exit(3)

    # display results
    for row in results:
        print(f'{row[0]}: {row[1]}')

    # close connection and cursor
    cursor.close()
    db.close()
