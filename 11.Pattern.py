'''
*
*  *
*  *  *
*  *  *  *

'''

x = int(input("Please enter number of Rows : " ))
for row in range(x):
    for col in range (row+1):
        print("*    ", end="")
    print()