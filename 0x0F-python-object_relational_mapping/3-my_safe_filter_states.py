#!/usr/bin/python3
""" displays all values in the states table without sql injection """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='locahost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()

    sql_query = """
    SELECT *
    FROM states
    WHERE name LIKE %s
    ORDER BY states.id
    """, (sys.argv[4])

    results = cursor.execute(sql_query)

    for row in results:
        print(row)

    cursor.close()
    db.close()
