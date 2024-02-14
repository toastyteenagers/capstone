# this class will store all fields of the user's data
# TODO: check that this seralizes nicely.
class UserFields:
    def __init__(self,name,vector,rhr,disability):
        self._name = name
        self._vector = vector
        self._rhr = rhr
        self._disability = disability # to be introduced later...
    def get_name(self):
        return self._name

    def get_vector(self):
        return self._vector

    def get_rhr(self):
        return self._rhr

    def get_disability(self):
        return self._disability

