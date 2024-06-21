#!/usr/bin/python3
"""
Python module that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
               FROM cities LEFT JOIN states ON states.id = cities.state_id \
              ORDER BY cities.id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for item in rows:
        print(item)

    cur.close()
    db.close()
