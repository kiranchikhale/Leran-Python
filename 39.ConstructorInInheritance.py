#Only Class A init will get call not Class B's
class A:
    def __init__(self):
        print("In A init")
    def fun1(self):
        print("Fun1")
    def fun2(self):
        print("Fun2")

class B:
    def __init__(self):
        print("In B init")
    def fun3(self):
        print("Fun3")
    def fun4(self):
        print("Fun4")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")
    def fun5(self):
        print("Fun5")
    def fun6(self):
        print("Fun6")

C1= C()
C1.fun1()
