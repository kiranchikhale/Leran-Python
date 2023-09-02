def factorial(num):
    result = 1
    for i in range(1,num+1,1) :

         result = result * i
         if i == num:
             print(result)
             return result


res = factorial(4)
print(res)