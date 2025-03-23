## Classes 
## OOP => Object Oriented Programming. Vs Functional Programming.
## Object Oriented Programming works with classes.
## A class is a blueprint/design for creating objects/types
## Classes can be called, and can take an argument OR NOT
## Some pillars of OOP include 
##      1) Inheritance : Classes can have parents from which they inherit certain properties/attributes/methods
##      2) Encapsulation : Classes can combine attributes and methods (behavior) together and only show how they can be used, but not how they are implemented
##      3) Polymorphism : We can refer to a group of child classes using their parent class
## Every class inherits from a parent call Object
## Like functions, classes are callable => They have to be called in order to be used.
## We create a class using the "class" keyword followed by the class name

## An object has attributes which form the state
## An objest has behavior => Methods

## Classes have an __init__ method that is called to initialize an object that is created from this class 
## Double underscore => dunder


class Person:
    '''This is called a DOCSTRING which is an documentation of a class'''

    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

kaba = Person("Emmanuel", "Kaba", 20, 175, 70)

print("This is Kaba Person")
print(kaba.first_name)
print(kaba.last_name)
print(kaba.age)
print(kaba.height)
print(kaba.weight)

louis = Person("Louis", "Ndango", 30, 175, 185)
print("\n")
print("This is Louis Person")
print(louis.first_name)
print(louis.last_name)
print(louis.age)
print(louis.weight)
print(louis.height)

print(type(louis))
print(type(kaba))