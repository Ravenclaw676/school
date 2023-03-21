"""this is an illustration of iteration vs recurcion"""
#iteration
arr = [3, 6, 2, 8, 1]
NUMBER = 0
for i, num in enumerate(arr):
    NUMBER += num
print(NUMBER)


# the recursion one
def add(numbers):
    """adds an array recursively"""
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add(numbers[1:])

print(add(arr))
