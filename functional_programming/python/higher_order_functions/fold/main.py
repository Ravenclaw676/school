"""this is an example of using reduce"""
from functools import reduce
LIST = [1,2,3,4,5]
print(reduce(lambda x, y: x+y, LIST, 0))
