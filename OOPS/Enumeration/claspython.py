# Define some example classes
class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"

class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Tweet!"

# List of classes (not instances)
class_list = [Dog, Cat, Bird]

# Iterate over the list of classes and create instances
for cls in class_list:
    instance = cls(f"{cls.__name__}Instance")
    print(f"{instance.__class__.__name__}: {instance.speak()}")


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Inheriting classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# List of classes, including inherited ones
animal_classes = [Dog, Cat]

# Create instances and print their behavior
for animal_class in animal_classes:
    animal = animal_class("Animal")
    print(animal.speak())    