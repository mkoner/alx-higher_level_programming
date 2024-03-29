#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(query)

    query_rows = cur.fetchall()
    for i in query_rows:
        print(i)
    cur.close()
    conn.close()
