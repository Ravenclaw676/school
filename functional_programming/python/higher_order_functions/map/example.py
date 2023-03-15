"""a program that doubles the number in list1 if list2 is true in the same index"""

list1 = [1,2,3,4,5,6]
list2 = [True, False, True, False, True, False]
def maptest(l1, l2):
    return map(lambda x, y: (x*2 if y else x), l1, l2)
print(list(maptest(list1, list2)))