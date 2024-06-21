#!/usr/bin/python3
"""
Python module that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE BINARY name = "{}" \
        ORDER BY id ASC""".format(searched))

    rows = cur.fetchall()
    for item in rows:
        print(item)

    cur.close()
    db.close()
