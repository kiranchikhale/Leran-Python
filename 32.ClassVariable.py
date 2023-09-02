class car:
    wheel = 4
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()

c1.mil = 12
car.wheel = 5

print(c1.mil)
print(c2.mil)
print(c2.wheel)
print(c1.wheel)
print(car.wheel)
