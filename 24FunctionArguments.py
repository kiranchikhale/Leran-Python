# KeyWords Arguments
def person(name, age):
    print(name)
    print(age)

person(age=45,name="anuradha")

def personDefaultArg(name="abc", age=18):
    print(name)
    print(age)

personDefaultArg("aradhana")

def addVariableLength(*b):
    add = 0
    for e in b:
        add = add +e
    print(add)
addVariableLength(1,2,4,5)

# *********** Pass multiple data with keyword *********

def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i,j)
person("Aradhaya", age=23,city="pune",mobile= 985033444)

