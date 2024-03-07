

class UserFields:
    def __init__(self,name,vector,rhr,disability,access = False):
        self._access = access
        self._name = name
        self._vector = vector
        self._rhr = rhr
        self._disability = disability # to be introduced later...
        self._missing_values = 0
        self.set_access()
        print(self._access)

    def get_name(self):
        return self._name

    def get_vector(self):
        return self._vector

    def get_rhr(self):
        return self._rhr

    def get_disability(self):
        return self._disability

    def get_access(self):
        return self._access

    def set_access(self):
        checks = 0
        if self._name != '':
            checks += 1
        #else:
            #print(self._name, ': Missing name')
        if len(self._vector) > 0:
            checks += 1
        #else:
            #print(self._name, ': Missing face encodings')
        if self._rhr != 0:
            checks += 1
        #else:
            #print(self._name, ': Missing resting heart rate')
        #Change check later based on what value will be represented
        if self._disability != 0:
            checks += 1
        #else:
            #print(self._name, ': Missing disability value')

        if checks == 4:
            self._missing_values = 0
            self._access = True
        else:
            self._missing_values = 4 - checks
            self._access = False