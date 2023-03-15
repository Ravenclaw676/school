"""used to illustarte partial functions using functools"""
from functools import partial # the library that allows partial functions

def function(X, Y):
    """a functions that divides y by x"""
    return Y/X

g = partial(function, 2) # makes 2 the x value
print(g(3))
