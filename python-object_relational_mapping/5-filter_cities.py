#!/usr/bin/python3
"""
Python module that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)
    cur = db.cursor()
    query = "SELECT cities.name \
               FROM cities LEFT JOIN states ON states.id = cities.state_id \
              WHERE states.name LIKE BINARY %s \
              ORDER BY cities.id ASC"
    cur.execute(query, (state,))

    rows = cur.fetchall()
    result = ""
    for item in rows:
        for value in item:
            result += value + ", "
    result = result[:-2]
    print(result)

    cur.close()
    db.close()
