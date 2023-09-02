# List can store ditterent type of data
# List is Mutable

num = [25,12,36,95,14]
# print(num[3])
# print(num[2:])
# print(num[:2])
# print(num[-4])
#
# names = ["navin","Kiran","shakti"]
# values = [9.5,"Navin",25]
# mil = [num,values]
# print(mil)

num.append(45)
print(num)

num[0]=100
print(num)

num.insert(2,66)
print(num)

num.remove(36)
print(num)

# num.pop(3)
# print(num)
# num.pop(-2)
# print(num)
# num.pop()
# print(num)

del num[2:]
print(num)

num.extend([45,333,444,666,777])
print(num)

print(min(num))
print(max(num))
print(sum(num))
num.sort()
print(num)

