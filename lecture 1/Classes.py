# Car class 
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

# Creating objects of the Car class
my_car = Car("red", "Toyota")
your_car = Car("blue", "Honda")

# Calling methods on objects
my_car.drive()  # Output: The red Toyota is driving.
your_car.drive()  # Output: The blue Honda is driving.


#Person class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) says woof!")

# Creating objects of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")

# Calling methods on objects
dog1.bark()  # Output: Buddy (Golden Retriever) says woof!
dog2.bark()  # Output: Max (Poodle) says woof!
