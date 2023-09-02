a = 13
# def fun1():
#     a = 3
#     print("In Fun :",a)
#
# fun1()
# print("OutSide Function :",a)

print("***************Fun2*****************")
def fun2():
    global a
    a = 3
    print("In Fun :",a)
fun2()
print("OutSide Function" , a)

print("***************Fun3*****************")
def fun3():
    a = 3
    x = globals()['a']
    globals()['a'] = 5
    print("In Fun :",a)

fun3()
print("OutSide Function" , a)