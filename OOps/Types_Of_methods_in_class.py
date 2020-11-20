class Student:
    
    school = 'ABC School'
    
    def __init__(self, marks1, marks2, marks3):
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3
    
    # mutators methods (setter)
    # accessor methods (getter)
    
    # instance methods
    def get_marks1(self):
        return self.__marks1

    def get_marks2(self):
        return self.__marks2

    def get_marks3(self):
        return self.__marks3

    def avg(self):
        return (self.get_marks1() + self.get_marks2() + self.get_marks3()) / 3
    
    # class methods
    @classmethod
    def get_school(cls):
        return cls.school
    
    # static methods
    @staticmethod
    def info():
        print('This is student class in abc module...')

s1 = Student(10, 20, 30)
print(s1.avg())

print(Student.get_school())

Student.info()