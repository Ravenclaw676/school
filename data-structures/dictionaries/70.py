countries = ("iran", "iraq", "syria", "afganistan", "pakistan")
print(*countries)

country = int(input("enter an index: "))
print(countries[country - 1])