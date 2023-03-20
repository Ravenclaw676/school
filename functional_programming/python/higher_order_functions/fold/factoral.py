"""a functions to create factoral recursivly using lambda"""
from functools import reduce

def fact(n):
    """does factoral """
    return reduce(lambda x,y: x*y, range(1, n+1))

print(fact(1000))
