class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class with constructor
person1 = Person("Alice", 30)

# Accessing attributes initialized by the constructor
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

# Calling a method on the object
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
