from datetime import datetime
from marshmallow import Schema, fields, post_load


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
        self.avgHR = rhr
        self.disability = disability
        self.doc = doc
        self.dateOfCreation = doc
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

    def get_avgHR(self):
        return self.avgHR

    def get_disability(self):
        if self.disability != 0:
            return "yes"
        else:
            return "no"

    def get_dateOfCreation(self):
        return self.dateOfCreation

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

    def set_avgHR(self, rhr):
        self.avgHR = rhr

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

    result = schema.dump(user)
    print(result)

# createUser("Owen", [1234], 95, 0)
# user = UserSchema()
# result = user.load("Owen", [1234], 95, 0)
