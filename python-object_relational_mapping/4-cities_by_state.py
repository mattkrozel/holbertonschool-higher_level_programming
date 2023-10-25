#!/usr/bin/python3
'''
script lists all cities
'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
        rows = cur.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
