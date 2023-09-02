def greet():
    print("******** Good Morning ***********")
greet()

def add_sub( x ,y):
    add = x + y
    sub = x - y
    return add, sub

res1, res2 = add_sub(7,3)
print(res1, res2)