class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def Sum(self,a = None,b= None,c= None ):
        sum= 0
        if(a != None and b!= None and c !=None):
            Sum = a+b+c
        elif a!= None and b !=None:
            Sum = a+b
        else:
            Sum =a
        print("Sum : {}".format(Sum))

s1 = Student(1,2)
s1.Sum(1,2,3)
s1.Sum(1,2)
s1.Sum(1)
