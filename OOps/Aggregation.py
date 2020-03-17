class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def calculateSalary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.sal_obj = salary

    def total_salary(self):
        return self.sal_obj.calculateSalary()

salary = Salary(15000, 1000)
emp = Employee('Max', 25, salary)
print(emp.total_salary())
