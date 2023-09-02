# Static method is not related to class od object
#Class method can access class variable but Static method do not
class Student:
    school = "My School"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def Avg(self):
        return (self.m1+self.m2+self.m3)/3

    @staticmethod
    def info():
        print("This is Student  class")


Student.info()
