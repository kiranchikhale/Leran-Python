#Tuple is immuatable (Rounded Brackets)
#iteration is faster in tuple then in List
tup = (6,21,36,6,14,6,45)
print(tup[1])
print(tup.count(6))

for i in range(len(tup)):
    print(tup[i])
print("*****************")
for j in tup:
    print(j)