# Array should have all the elenent of same type
from array import *
#import array as arr

#v= arr.array('i',[5,6,3,1,2])
v = array('i',[5,6,3,1,2])
# for k in v:
#     print(k)
# print("****************")
# for k in range(len(v)):
#     print(v[k])

#Copy an array

#mynewArray = arr.array(v.typecode,[a for a in v])
mynewArray = array(v.typecode,[a for a in v])
for g in mynewArray:
    print(g)