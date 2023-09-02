a = 5
b = 2
try:
    print("Resourse Open")
    print(a/b)
    k = int(input("Enter a Number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey ,you can not divide a Number by Zero  :",e)
except ValueError as e:
    print("Invalid Input :", e)
finally:
    print("Resourse Closed")
