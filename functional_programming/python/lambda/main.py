"""lambda is used to create a function using functional programming """
def myFunc(n):
    """an example use of lambda"""
    return lambda a : a * n 

mytripler = myFunc(3)
print(mytripler(11))
