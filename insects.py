import random 
class insects:
    def  __init__(self):
     self.__wings = 2
     self.__legs = 4
     self.__flight = 0
    
    def get_flight(self):
        self.__flight = random.randint(1,10)
        return self.__flight

my_bug = insects()
print(my_bug.get_flight())
    