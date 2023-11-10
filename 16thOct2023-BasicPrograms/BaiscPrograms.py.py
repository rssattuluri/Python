# Difference between = and == operators:

x = 10
# Assignment in Python


#equality comparison.
y = 5
z = 5
result = (y == z)
print(result)


#** operator:

a = 2
b = 3
result = a ** b  # This will be 8 (2 raised to the power of 3)
print(result)


# ^ operator:

x = 5  # binary: 0101
y = 3  # binary: 0011
result = x ^ y  # This will be 6 (binary: 0110)

# Calculate the area of a circle
import math


radius = float(input("Enter the radius\n"))
area = math.pi* (radius **2)

print(area)

# Compare two numbers:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
print(f"{num1} is {result} {num2}")

# Find the maximum of three numbers using the ternary operator:

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_number = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {max_number}")

# Calculate square and cube of a given number:

number = float(input("Enter a number: "))
square = number**2
cube = number**3
print(square)
print(cube)

# Condition
# Set of rules - > age > 18 then you can watch a movie

age = float(input("Enter your age"))
print(age)

# if this
#     else then

if age > 18:
    print("You can watch a movie")
else:
    print("You can't ")

x = 20
y = 10

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")
# Problem to find the MAX three

a = 10
b = 20
c = 13

output = None

if a > b and a > c:
    output = a
elif b > a and b > c:
    output = b
else:
    output = c

print(output)

# Loop

# Repeat a block of code multiple times

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# for int i = 1; i< 10 ; i++
for x in range(1,10,1):
    print(x)

# range(start,stop, step)
# while

i = 0
while i < 5: # condition - true or false
    print(i)
    i = i + 1 # increment
    #i++


