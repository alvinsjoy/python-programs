class Student:
    def __init__(self, name):
        print("This is parameterized constructor")
        self.name = name
    def show(self):
        print("Hello " , self.name)
s1 = Student("Rahul")
s1.show()
s2 = Student("Raj")
s2.show()