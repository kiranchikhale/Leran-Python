'''
*  *  *  *
*  *  *
*  *
*
'''

x = int(input("Please enter number of Rows : " ))
for row in range(x):
    for col in range (x-row,0,-1):
        print("*    ", end="")
    print()