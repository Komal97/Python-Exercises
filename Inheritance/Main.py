from Rectangle import Rectangle
from Triangle import Triangle

rect = Rectangle()
tri = Triangle()

rect.set_values(40,50)
tri.set_values(20,50)

rect.set_color('red')
tri.set_color('green')

print('Rectangle ', rect.get_color())
print('Triangle ', tri.get_color())
print('Rectangle ', rect.area())
print('Triangle ',tri.area())