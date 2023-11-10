# Factorial

# Loop
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
# 1! -> 1

number = int(input("Enter the a number\n"))
if number < 0:
    print("Factorial is not possible!! for negative")
else:
    fact = 1
    for i in range(1, number + 1): #(0, len-1)
        fact = fact * i

print("Fact is -> ", fact)


# Fibonaci series
# 0,0+1, 0+1+1,
# n = 7


a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b


# Match
# Similar to Switch in Java

number = int(input("Enter a numer\n"))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case _: #Nothing is mathcing, I will run
        print("No idea")

name = input("Enter your name\n")

match name:
    case "pramod":
        print("Welceome pramod")
    case "lucky":
        print("Welcome lucky")
    case "amit":
        print("Amit")
    case _:
        print("welcome, there")


#match statement > 3.10 (Pyton, 3.11)

number = int(input("Enter a Numer Int\n"))

match number:
    case 10:
        print("10")


# Functions

output = max(1,3) # Built in function
print(output)

# Block of Code
# 1. Built in - Which are created by the Python Guys
# for you so that you can use them without
# creating your own


# 2. Custom Function - You can create a func which is a block of code, anyone can reuse it


a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
print(a+b)

# Written some code

def sum(a,b):
    return a+b

a = int(input("Enter a\n"))
b = int(input("Enter b\n"))
print(sum(a,b))

print(sum(34,45))


# 10,000 lines

print(sum(45,67))



def sayHello():
    print("Hi")


sayHello() # Call this func

def sayHelloToYou(name):
    print("You name is ", name)


sayHelloToYou("Pramod")

min(34,32)


def inCompleteFunction(*args):
    print(type(args))
    # This code is incomplete
    print("Hi, I am working on it, Please wait for 100 years to complete")
    pass


inCompleteFunction(1)
inCompleteFunction(1,2)
inCompleteFunction(1,2,3)
inCompleteFunction(1,2,3,4,6,6,6,6,6,6,6,6,6,)
