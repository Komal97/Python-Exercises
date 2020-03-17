# class Car:
#     def __init__(self):
#         print("the __init__ is called")
#
# ford = Car()
# honda = Car()
# audi = Car()
# ford.speed = 200
# honda.speed = 220
# ford.color = 'red'
# honda.color = 'blue'
# print(ford.speed)
# print(ford.color)


class Car:

    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
        print("the __init__  is called")

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(240, 'black')
honda = Car(220, 'blue')

ford.set_speed(300)
print(ford.get_speed())

ford.set_color('red')
print(ford.get_color())

# print(ford.speed)
#print(ford.color)


