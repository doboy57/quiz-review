from datetime import date


class Student:
    def __init__(self, id, name, dob, classification):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''
    def return_classification(self):
        return self.__classification
    def return_age(self):
        return self.__age

    def return_registration(self):
        return self.__register

    def register(self):
        if self.__classification == 'freshman':
            self.register = '9/11/21 through 9/12/21'
        elif self.__classification == 'sophmore':
            self.register = '9/13/21 throguh 9/14/21'
        elif self.__classification == 'junior':
            self.register = '9/15/21 through 9/16/21'
        elif self.__classification == 'senior':
            self.register = '9/17/21 throguh 9/18/21'
        else:
            self.register = 'classification not found'

    def calc_age(self):
        t = date.today()
        birthdate = self.__dob.split("/")
        birthdate_year = int(birthdate[2])
        age = t.year - birthdate_year
        self.__age = age
