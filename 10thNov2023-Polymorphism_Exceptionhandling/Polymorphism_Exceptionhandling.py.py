# Poly
# ABC
# Exception

# Polymorphism - object-oriented programming (OOP)
# object -> behave differently based on the sti.
# Person -> Amit, Pramod -> talk() , Amit can talk in hindi, pramod can talk in english

class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        super().area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())


shape3 = Shape()
shape3.area()


# Method Overriding - Same name in the parent and child
# child always overide the parent functions
# super means call my parent function

class Animal:

    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def __init__(self):
        pass
    def sound(self):
        super().sound()
        print("Dog Sound")




# animal = Animal()
# animal.sound()


dog = Dog()
dog.sound()

# Method Overloading:
# Python does not support method overloading in the traditional sense
# Same name of a function with different Parameter

class MathUtil:
    def add(self, a, b=0, c=0):
        return a + b + c


math = MathUtil()
# op11 = math.add("pramod")
# op11 = math.add()
op0 =  math.add(1)
op1= math.add(1, 2)
op2 = math.add(1, 2,3)
print(op0)
print(op1)
print(op2)
# math.add(1, 2, 3)  ## Python does not support method overloading in the traditional sense


class Browser:
    def __init__(self, browser):
        self.browser = browser

    def openBrowser(self, browser="chrome"):
        print("Write the code to open the Browser -> " + browser)


b = Browser("Firefox")
b.openBrowser()


# Abstraction - OOPs
# Hiding the details and showing the what is required

# Car ->  start the engine ->  put the gear -> start driving
# -> Do you know How engine is started? , How gear box was managed?
# hide the implementation and show only the important details


# to represent complex systems by simplifying and hiding unnecessary details

# ABC -> ? Abstract Base Class
# Abstract base Methods

# Shape -> Rectangle, Circle
# Shape -> perimeter, area

# Animal(speak) -> Dog, Cat, Toger( roar)

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bow Bow"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Tiger(Animal):
    def sound(self):
        return "Roar Roar!!, Grrrr!!!"


dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

tiger= Tiger()
print(tiger.sound())


# animal = Animal()


class A:
    def print(self):
        print("A")


class C:
    def print(self):
        print("C")


def B():
    print("B")


from Lab133 import A,B, C
from Lab131 import Browser

# calling Class A
# calling Method B

a = A()
a.print()

B()

C().print()

Browser("chrome").openBrowser()

a = 10
b = 0



# Exception
# An exception is an event that occurs during the execution of a program
# that disrupts the normal flow of instructions.

try:
    c = a/b
except Exception as error:
    print(error)
    
a = int(input("Enter your A number"))
b = int(input("Enter your B number"))
try:
    c = a/b
    print(c)
except Exception as error:
    print("You are diving the Value of A with zero, Please don't do it", error)


# I want to use the PIE, Satish has already written ?
from Satish import SatishClass


satish = SatishClass()
# satish.__to_Cal_PIE()
satish.to_Cal_PIE_2()

class SatishClass:
    def __private_toilet_of_satish(self):
        print("PIE value", 3.14)

    def pub_satish_toilet(self):
        print("PIE value", 3.14 * 2)
