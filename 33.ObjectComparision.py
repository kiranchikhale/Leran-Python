# Class Constructor
class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def update(self):
        self.age =30

    def compare(self,other):
        if(self.age == other.age):
            return True
        else:
            return False

com1 = Person(16,"Aarti")
com2 = Person(16,"amit")
if com1.compare(com2):
    print("They are of same age")
else:
    print("They are of different age")


