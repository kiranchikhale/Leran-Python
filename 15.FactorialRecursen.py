
def factorial(num):
    result = 1
    if num == 1:
       return 1

    result = num * factorial(num-1)
    return result



res = factorial(4)
print(res)