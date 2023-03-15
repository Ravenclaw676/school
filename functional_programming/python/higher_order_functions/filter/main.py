"""filters a list for odd number"""

ip = [1,2,3,4,5,6]
op = filter(lambda x:x%2==1, ip)
print(list(op))