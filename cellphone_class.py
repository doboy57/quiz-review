class Cellphone:
    def __init__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufact): #mutator
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

    def get_manufact(self): #accessor
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
my_phone = Cellphone('apple', 'iphone', 750)
print(my_phone.get_manufact())
print(my_phone.get_model())
print(my_phone.get_retail_price())

