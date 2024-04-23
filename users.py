from datetime import datetime
from marshmallow import Schema, fields, post_load
import json
import sqlite3


# from test import add_database
class newUser:

    def __init__(self, name, encodings, rhr, disability, level=0, uses=[], doc=datetime.now()):
        self.level = level
        self.name = name
        self.first_name = self.name.split(' ')[0]
        self.last_name = self.name.split(' ')[-1]
        if len(self.name.split()) > 2:
            self.middle_name = ' '.join(self.name.split()[1:-1])
        else:
            self.middle_name = ""
        self.encodings = encodings
        self.rhr = rhr
        self.disability = disability
        self.doc = doc
        # self.dateOfCreation = doc
        self.uses = uses

    def add_use(self):
        temp = datetime.now()
        self.uses.append([temp.strftime("%B %d, %Y"), temp.strftime("%I:%M:%S %p")])

    def get_name(self):
        return self.name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_encodings(self):
        return self.encodings

    def get_rhr(self):
        return self.rhr

    def get_disability(self):
        if self.disability != 0:
            return "yes"
        else:
            return "no"

    def get_dateOfCreation(self):
        return self.doc

    def get_use_history(self):
        return self.uses

    def get_level(self):
        return self.level

    def set_name(self, name):
        self.name = name
        self.first_name = self.name.split(' ')[0]
        self.last_name = self.name.split(' ')[-1]
        if len(self.name.split()) > 2:
            self.middle_name = ' '.join(self.name.split()[1:-1])
        else:
            self.middle_name = ""

    def set_encodings(self, encodings):
        self.encodings = encodings

    def set_rhr(self, rhr):
        self.rhr = rhr

    def set_disability(self, disability):
        self.disability = disability


class administrator(newUser):
    def __init__(self, name, encodings, rhr, disability, password="admin"):
        super().__init__(name, encodings, rhr, disability)
        self.level = 1
        self.password = password

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password


class UserSchema(Schema):
    name = fields.String()
    encodings = fields.List(fields.Integer())
    rhr = fields.Integer()
    disability = fields.Integer()
    uses = fields.List(fields.String())
    doc = fields.String()
    level = fields.Integer()

    @post_load
    def create_user(self, data, **kwargs):
        return newUser(**data)


def createUser(name, encodings, rhr, disability, level=0, uses=[], doc=datetime.now()):
    user_data = {
        "name": name,
        "encodings": encodings,
        "rhr": rhr,
        "disability": disability,
        "level": level,
        "uses": uses,
        "doc": doc.strftime("%B %d, %Y %I:%M")
    }
    schema = UserSchema()
    user = schema.load(user_data)
    # print(user.get_first_name())
    result = schema.dump(user)
    print(result)
    add_to_database(result)


def add_to_database(data):
    data['encodings'] = json.dumps(data['encodings'])
    data['uses'] = json.dumps(data['uses'])

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE encodings=?", (data['encodings'],))
    if len(c.fetchall()) != 0:
        print("Duplicate user will not be added to database")
    else:
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", (
        data['name'], data['encodings'], data['rhr'], data['disability'], data['uses'], data['doc'], data['level']))

    conn.commit()
    conn.close()


def search_database(encodings):
    encodings = json.dumps(encodings)
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE encodings=?", (encodings,))
    print(c.fetchone())
    conn.commit()
    conn.close()


def delete_from_database(name, encodings):
    encodings = json.dumps(encodings)

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE name= ? AND encodings= ?", (name, encodings))
    conn.commit()
    conn.close()


def load_users():
    active_users = []
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    users_in_database = c.fetchall()

    for i in users_in_database:
        schema = UserSchema()
        user_data = {
            "name": i[0],
            "encodings": json.loads(i[1]),
            "rhr": i[2],
            "disability": i[3],
            "level": i[6],
            "uses": json.loads(i[4]),
            "doc": i[5]
        }

        user = schema.load(user_data)
        active_users.append(user)

    conn.commit()
    conn.close()

    return active_users


# createUser("Alex Ram", [1235], 95, 0)

# conn = sqlite3.connect('users.db')
# c = conn.cursor()

# c.execute("SELECT * FROM users WHERE name='Owen'")

# Comment out
# c.execute("SELECT * FROM users")
# print(c.fetchall())

# delete_from_database('Alex', [1235])

# c.execute("SELECT * FROM users")
# print(c.fetchall())


# search_database([1235])
# fetchone
# fetchall
# fetchmany

# conn.commit()
# conn.close()


#load_users()