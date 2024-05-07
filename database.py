import sqlite3

#conn = sqlite3.connect('users.db')

#c = conn.cursor()

#c.execute("""CREATE TABLE users (
#          name text,
#          encodings text,
#          rhr integer,
#          disability integer,
#          uses text,
#          doc text,
#          level integer
#        )""")

#conn.commit()

#conn.close()

conn = sqlite3.connect('admins.db')

c = conn.cursor()

c.execute("""CREATE TABLE admins (
          name text,
          encodings text,
          rhr integer,
          disability integer,
          uses text,
          doc text,
          level integer,
          password text
)""")

conn.commit()

conn.close()

