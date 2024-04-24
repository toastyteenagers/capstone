
import sqlite3
# this file needs to be run ONCE upon init.
conn = sqlite3.connect('users.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
          name text,
          encodings text,
          rhr integer,
          disability integer,
          uses text,
          doc text,
          level integer
        )""")

#def add_database(data):
#    c.execute("INSERT INTO users VALUES (data['name'], data['encodings'], data['rhr'], data['disability'], data['uses'], data['doc'], data['level'])")

#c.execute("INSERT INTO users VALUES ('name', [1234], 90, 0, [], 'today', 1)")


#c.execute("INSERT INTO users VALUES ('Owen', [1234], 95, )")

#createUser("Owen", [1234], 95, 0)
conn.commit()

conn.close()