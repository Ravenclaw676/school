file = open("names.txt", "r")
for name in file:
    print(name)
file.close()