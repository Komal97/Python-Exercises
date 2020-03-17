class Parent:
    def __init__(self, name):
        print("Parent __init__", name)

class Parent2:
    def __init__(self, name):
        print("Parent2 __init__", name)

class Child(Parent):
    def __init__(self):
        print("Child __init__")
        # super().__init__('Komal')
        Parent.__init__(self, 'Hi')
        Parent2.__init__(self, 'Komal')

#parent = Parent('Hi')
child = Child()
