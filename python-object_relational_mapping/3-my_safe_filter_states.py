#!/usr/bin/python3
'''
script takes arg and shows values in states where name marches arg
'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC", {'name': sys.argv[4]})
        rows = cur.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
