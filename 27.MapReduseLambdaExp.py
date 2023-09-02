from functools import reduce
nums = [3,2,6,8,4,6,2,9] #list
def is_even(n):
    return n%2 == 0

#evens = list(filter(is_even,nums))
evens = list(filter(lambda a: a%2==0,nums))
print(evens)

double = list(map(lambda n : n*2,evens))
print(double)

sum = reduce(lambda a,b: a+b, double)
print(sum)