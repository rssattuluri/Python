"""
#if else
# if condition
a = 100
if a > 50:
    print("a is bigger than 50")

#if + else
a = 100
if a > 50:
    print("a is bigger")
else:
    print("a is smaller")
print("end of if else") # This line is not part of if+else as not following indentation, so always in output

#if + elif + else (Program to find greatest number between 3 numbers)
a = 50
b = 100
c = 150
if a > b > c:
    print("a is bigger")
elif a < b < c:
    print("c is bigger")
else:
    print("b is bigger")
print("end of if else")

# while loop
a = 1           # Initialization/start
while a <= 5:   # Condition/stop
    print(a)
    a += 1      # Incrementation/jump
print("Loop is over")

# For loop
# for + str
# fetches letter by letter
for abc in "Hello world":
    print(abc)

# for + list
# fected element by element
for abc in [1, 2.33, "Hello world", 66, 100]:
    print(abc)

# for + set
for abc in {1, 2, "Hello", 2.33, "+"}:
    print(abc)

# for + tuple
for abc in (100, 2, 33.33, "Hello"):
    print(abc)

# Functions
def Ramya():          # function creation
    print("Hi Ramya")
def Naren():
    print("Hi Naren")
Naren()
Ramya()               # function calling

# function + arguments
def Ramya(x,y):
    print("Hello",x,y)
Ramya(10,20)

# function + default arguments
def Ramya(x=0,y=0):
    print("Hello",x,y)
Ramya(34,62)

# Library
# math
import math
x = math.sqrt(25)
print(x)

#Calling function from other files/other library
import Lab01
Lab01.myfun()

"""