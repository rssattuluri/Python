class BankAccount:
    def __init__(self):
        self.balance = 0 # Instance Variable ( You can access it via only Object)
        self.__private_var = 100

    def deposit(self, amount):  # Public Function
        # self.balance = self.balance + amount
        self.balance += amount

    def _withdraw(self, amount):  # Protected
        self.balance -= amount

    def __show_balance(self):
        print("Your Bal", self.balance)

    def IS_Auth_True_show_bal(self, isAuth):
        if isAuth:
            self.__show_balance()
        else:
            print("You are not Auth")

    def do_withdraw_by_bank_manager(self,amount):
        self._withdraw(amount=amount)


jp_chase = BankAccount()
jp_chase.deposit(1000)
jp_chase._withdraw(499)  # Not a Good practice ( Protected)
# jp_chase.__show_balance()

# Never use this
jp_chase._BankAccount__private_var = 100
print(jp_chase._BankAccount__private_var) # Super Bad Pratice - Python allow this , Java

# Write the code to Auth - Dev
# jp_chase.IS_Auth_True_show_bal(True)
jp_chase.IS_Auth_True_show_bal(False)


# Public - Variable - Don't Mention anything
# Protected - _
# Private - __

# Variable and Function


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        if name == "John":
            print("Don't set the name")
        else:
            self.__name = name

    def print_details(self):
        print("You details", self.__name, self.__age)


person = Person("Amit", 34) # It will call the  __init__ with name,age
person.print_details()
# print(person.__name) # Private ?

# How to change it Get and Set ?
# Fetch - Get
# Set the value  - Constuctor


person.set_name("John")

name = person.get_name()
print(name)

person.print_details()




class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Weak Password")

    def print_len(self):
        print("Your Password Len is ", len(self.__password))


pwd = Password("Hacker123")

pwd.public_var

pwd.print_len()
pssd = pwd.get_password(False)
print(pssd)

# pwd.__password

pwd.set_password("Pramod123123")
pwd.print_len()


# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def car(self):
        print("Lambo")
    def speak(self):
        print("Animal Speak!")


class Dog(Animal):
    pass



dog = Dog()
dog.speak()


# Single Inheritance - 90%
# Use the properties, variables and methods of your base class or parent class by the sub class or son class




class Father:
    bank_bal =  100

    def one_bhk(self):
        print("Use it son")


class Son(Father):
    pass # I wil write the code in future!! Skip


s = Son()
s.one_bhk()
print(s.bank_bal)

# Multilevel Inheritance
#Level - GF -> F -> S


class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "Child's method"

child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())


# Hierarchical Inheritance:
class Vehicle:
    def info(self):
        return "This is a vehicle."


class Car(Vehicle):
    def info(self):
        return "This is a car."


class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle."


car = Car()
bicycle = Bicycle()
print(car.info())
print(bicycle.info())


# F, M -> 5, 5 from both

class Father:
    def father_money(self):
        return "5"


class Mother:
    def mother_money(self):
        return "5"


class Son(Father, Mother):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())


# Hybrid Inheritance

# multiple types of inheritance, such as single, multiple, and multilevel inheritance.


class A:
    def methodA(self):
        return "Method A"

class B(A):
    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"


class D(B, C):
    def methodD(self):
        return "Method D"


d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())


def get_value():
    val1 = 42
    val2 = "Hello"
    return val1,val2


op = get_value()
print(op)

class GF:
    def car(self):
        return "Old car"


class F(GF):
    pass
    # def car(self):
    #     return "honda civic"


class S(F):
    # def car(self):
    #     return "Lambo"
    pass


son = S()
print(son.car())
