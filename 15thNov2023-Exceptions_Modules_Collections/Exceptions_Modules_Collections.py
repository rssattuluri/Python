# Exception
# abnormal event during the execution program, But ut can handled

# Error - specific code ->  1 gb -> 1.2 gb ? StackOverFlow
# 10 , 12 - Error -> It very diffcult to overcome
# MemoryError - Error -> Restart, retry

# Java -> Python
"""
print("Insert the Card")

try:
    a = 10 / 0
except Exception as e:
    print("XX Error due to 10/0")

print("Take the Card")



a = 10
b = 90
# try except
# try:
#     a = 10 / 0
# except ZeroDivisionError as e:
#     print(e)

# try except and nested except
try:
    num1 = int(input("Enter a Number"))
    num2 = int(input("Enter a Number"))
    result = num1 / num2
except ValueError:
    print("InValid Input")
except ZeroDivisionError:
    print("Num2 is zero")
else:
    print(f"Result {result}")
finally:
    print("I will be always executed!!")

# num 1 - 10, pramod (ValueError)
# num 2 - 0

# ZeroDivisionError
# ValueError


# else and finally
# Modules

def Util():
    print("Here we have some Utils written")


class Util2:
    def printMe(self):
        print("Hello from Util2")

from Lab140 import *

Util()
Util2.printMe("d")

def this_is_main_func_as_per_python_now():
    print("Hello from main")


if __name__ == "__main__":
    this_is_main_func_as_per_python_now()


# JAVA -> main() - J
35 changes: 35 additions & 0 deletions 35
15_NOV_2023/Lab143.py
@@ -0,0 +1,35 @@
# Collection -

# list, dic, tuple, set, OrderedDict - Data Type

regular = (1, 2, 3)
# regular[0] = 20 # They are not mutable

print(regular[0])

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])



person = Person(name="Pramod", age=34, gender="M")

print("Name", person.name)
print("Age", person.age)
print("Gender", person.gender)


class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name}")


person2 = Person2("Pramod", 23, "M")
person2.print_details()

#Python Loops, List, Dict, Set [x]
"""

# API Automation
# What is API? (Postman)

# 1.HTTP Fundamentals
# 2.API Testing with 1 project Postman
# 3.Lib in Python
#   1. Request - API Request
#   2. PyTest  - Testing Framework, Run your Test cases
#   3. Reporting - Allure Report
#   4. File Handling, CSV, Excel, Yaml, Read JSON file
#   5. Python Loops, List, Dict, Set.
# Project #2


# Web Automation
# 1. Selenium + POM
# 2. PyTest
# 3. Reporting
# 4. File & Misc Concepts are same as in APIs
# Automation - Project #1
