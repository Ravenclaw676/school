class Employee:
    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

emp_1 = Employee("Corey", "Schafer", "Corey.Schafer@company.com", 50_000)
emp_2 = Employee("test", "user", "test.user@company.com", 60_000)

print(emp_1)
print(emp_2)

print(emp_1.email)