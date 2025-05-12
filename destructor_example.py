class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Object {self.name} created")
        
    def __del__(self):
        print(f"Object {self.name} with age {self.age} is being destroyed")
        
# Create objects
obj1 = MyClass("First", 25)
obj2 = MyClass("Second", 30)

# Using objects
print(f"Working with {obj1.name} with age {obj1.age} and {obj2.name} with age {obj2.age}")
print(f'Sum of ages: {obj1.age + obj2.age}')
# Delete object explicitly
print("Deleting obj1...")
del obj1

# Create another object
obj3 = MyClass("Third", 35)

# obj2 and obj3 will be destroyed automatically when program ends
print("Program ending...") 