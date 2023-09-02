f1 = open('MyData.txt','r')
f2= open('abc.txt','w')
for data in f1:
    f1.write(data)

f3 = open("kk21.jpg","rb")
f4 = open("kk22.jpg","wb")
for data in f3:
    f4.write(data)