numofElement  = int(input("Please Enter Number of Element in Series"))
num1 = 1
num2 = 1
print(num1, )
print(num2, )
for  i in range(numofElement-2):
    i    = 1
    temp = num1
    num1 = num2
    num2 = temp + num1
    print(num2)