class Car:
    name = "Pramod" # Class Varaible

    def __init__(self,make,model): # Default con
        self.make = make  #  Instance Vairable
        self.model = model # Instance Vairable
        print("I will be called first")

    def start_engine(self):
        print("Starting a car", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()
car2.start_engine()

print(id(car1))
print(id(car2))


# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them

class Person:

    def __init__(self):
        print("Can I use you?")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You created an Object with name and age")

    def printDetails(self):
        print("Your details are", self.name, self.age)

    def printDetails2(self):
        print("Your details are", self.name * 2)


amit = Person("amit", 34)
amit.printDetails()

nikhil = Person("nikhil", 45)
nikhil.printDetails()


# Encapsulation
# Data Members(Attributes) and Methods Together in a class
# Person -> name,age and eat(), sleep()


# Visibility

# !! Public Member
# Public members have no special naming convention in Python and
# are accessible from anywhere.
# They can be accessed directly from outside the class and other modules.


# ----------------------
# !! Protected Member
# Protected members are denoted by a single underscore prefix (_).
# They can still be accessed from outside the class, but it is considered a
# best practice not to do so directly.


# ----------------------
# !! Private  Member
# Private members are denoted by a double underscore prefix (__).
# Private members are intended to be used within the class only.


class MyClass:

    def __int__(self):
        self.public_var = 10
        self._protected_var = 12
        self.__private_var = 15

    def public_method(self):
        print("This is Public Method")



    def _protected_method(self):
        print("This is Protected Method")
        print(self.__private_var)

    def __private_method(self):
        print("This is a private method.")



obj = MyClass()

# Public
obj.public_method()


class Myclass:

    def __int__(self):
        self.__private_toilet = "Private Toilet Only Pramod Allowed"
        self._protected_attribute = 42
        self.public_var = 55

    def __private_method(self):
        return "This is a private method."


obj = Myclass()
#print(obj.__private_toilet)

# Learn about the Private, Protected and Public variables
