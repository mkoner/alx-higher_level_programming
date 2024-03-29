#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbs = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    c = dbs.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    dbs.close()
