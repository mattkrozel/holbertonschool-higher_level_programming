#!/usr/bin/python3
'''
script lists all cities of that state
'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY %(state_name)s ORDER BY cities.id ASC", {'state_name': sys.argv[4]})
        rows = cur.fetchall()
    if rows is not None:
        print(', '.join([row[1] for row in rows]))
