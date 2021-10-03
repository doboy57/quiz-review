class person:
    def __init__(self, name, address, telephone,):
      self.__address = address
      self.__telephone = telephone
      self.__name = name

    def print_person(self):
        print(self.__address)
        print(self.__telephone)
        print(self.__name)
class customer(person):
    def __init__(self, name, address, telephone,customer_number,on_list):
        person.__init__(self, name, address, telephone)
        self.__customer_number = customer_number
        self.__on_list = on_list

    
    def print_person(self):
        person.print_person(self)
        print(self.__customer_number)
        if self.__on_list:
            print('on mailing list: yes')
        else:
            print('on mailing list: no')

   