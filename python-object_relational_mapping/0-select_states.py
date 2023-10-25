#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    argument = sys.argv
    if len(argument) != 4:
        print('Usage: {} username password database_name'.format(argument[0]))
        exit(1)
    username = argument[1]
    password = argument[2]
    databasename = argument[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db = databasename, port=3306)
    curs=db.cursor()
    numberrows = curs.execute('SELECT * FROM states ORDER BY states.id;')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()