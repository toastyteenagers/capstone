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
            return "True"
        else:
            return "False"

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
    def __init__(self, name, encodings, rhr, disability, level=1, uses=[], doc=datetime.now(), password="admin"):
        super().__init__(name, encodings, rhr, disability, level, uses, doc)
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


class AdminSchema(Schema):
    name = fields.String()
    encodings = fields.List(fields.Integer())
    rhr = fields.Integer()
    disability = fields.Integer()
    uses = fields.List(fields.String())
    doc = fields.String()
    level = fields.Integer()
    password = fields.String()

    @post_load
    def create_admin(self, data, **kwargs):
        return administrator(**data)


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


def createAdmin(name, encodings, rhr, disability, password='Admin', level=1, uses=[], doc=datetime.now()):
    admin_data = {
        "name": name,
        "encodings": encodings,
        "rhr": rhr,
        "disability": disability,
        "level": level,
        "uses": uses,
        "doc": doc.strftime("%B %d, %Y %I:%M"),
        "password": password
    }
    schema = AdminSchema()
    user = schema.load(admin_data)
    # print(user.get_first_name())
    result = schema.dump(user)
    print(result)
    add_admin(result)


def add_to_database(data):
    data['encodings'] = json.dumps(data['encodings'])
    data['uses'] = json.dumps(data['uses'])

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE encodings=?", (data['encodings'],))
    conn2 = sqlite3.connect('admins.db')
    c2 = conn2.cursor()
    c2.execute("SELECT * FROM admins WHERE encodings=?", (data['encodings'],))

    if len(c.fetchall()) != 0:
        print("Duplicate user will not be added to database")
    elif len(c2.fetchall()) != 0:
        print("User already exists as admin")
    else:
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", (
        data['name'], data['encodings'], data['rhr'], data['disability'], data['uses'], data['doc'], data['level']))

    conn2.commit()
    conn2.close()
    conn.commit()
    conn.close()


def add_admin(data):
    data['encodings'] = json.dumps(data['encodings'])
    data['uses'] = json.dumps(data['uses'])

    conn = sqlite3.connect('admins.db')
    c = conn.cursor()
    c.execute("SELECT * FROM admins WHERE encodings=?", (data['encodings'],))

    conn2 = sqlite3.connect('users.db')
    c2 = conn2.cursor()
    c2.execute("SELECT * FROM users WHERE encodings=?", (data['encodings'],))

    if len(c.fetchall()) != 0:
        print("Duplicate user will not be added to database")
    elif len(c2.fetchall()) != 0:
        print("User already exists")
    else:
        c.execute("INSERT INTO admins VALUES (?,?,?,?,?,?,?,?)", (
        data['name'], data['encodings'], data['rhr'], data['disability'], data['uses'], data['doc'], data['level'],
        data['password']))

    conn2.commit()
    conn2.close()
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


def load_admins():
    active_users = []
    conn = sqlite3.connect('admins.db')
    c = conn.cursor()

    c.execute("SELECT * FROM admins")
    users_in_database = c.fetchall()

    for i in users_in_database:
        schema = AdminSchema()
        admin_data = {
            "name": i[0],
            "encodings": json.loads(i[1]),
            "rhr": i[2],
            "disability": i[3],
            "level": i[6],
            "uses": json.loads(i[4]),
            "doc": i[5],
            "password": i[7]
        }

        user = schema.load(admin_data)
        active_users.append(user)

    conn.commit()
    conn.close()

    return active_users


# createUser("Hayden Test", [12], 95, 0)
# createUser("Owen Test", [1235], 95, 0)
# createUser("Alex Test", [1234], 95, 0)
# createAdmin("Owen Boxx", [123], 95, 0, 'team11')
# createUser("test", [4322], 95, 0)
# createAdmin("Owen Boxx", [4322], 95, 0, 'team11')
#conn = sqlite3.connect('users.db')
#c = conn.cursor()
#conn2 = sqlite3.connect('admins.db')
#c2 = conn2.cursor()
# c.execute("SELECT * FROM users WHERE name='Owen'")

# Comment out
#c.execute("SELECT * FROM users")
#print(c.fetchall())

#c2.execute("SELECT * FROM admins")
#print(c2.fetchall())

#conn.commit()
#conn.close()

#conn2.commit()
#conn2.close()

# delete_from_database('Alex', [1235])

# c.execute("SELECT * FROM users")
# print(c.fetchall())


# search_database([1235])
# fetchone
# fetchall
# fetchmany


load_users()