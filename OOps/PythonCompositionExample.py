class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def calculateSalary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.sal_obj = Salary(pay, bonus)

    def total_salary(self):
        return self.sal_obj.calculateSalary()

emp = Employee('Max', 25, 15000, 10000)
print(emp.total_salary())
