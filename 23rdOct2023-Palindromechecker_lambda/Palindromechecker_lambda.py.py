# Function

def Hello():
    print("Code that you want to execute")


Hello() # Callling of the functions# user_input = input("Enter the inpout String\n")


# Palindrome
# Reverse the String and match with the old String it should be same.
# 1 By using a Traditional method
# 2 Built in functions

def reverse_string(input_string):
    reverse_str = ""
    for c in input_string:
        reverse_str = c + reverse_str
    return reverse_str


original_str = "NAMAN"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not")
    
original_str = "NAMAN"


def is_palindrome(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
        print("Palindrome")
    else:
        print("It is not")


is_palindrome(original_str)


original_str = "PRAMOD"


def rev_string(original_str):
    return ''.join(reversed(original_str))


rev_str = rev_string(original_str)
print(rev_str)

# digit = 12345
# mod1 = digit%10
# print(mod1)
# digit = 1234
# mod2 = digit%10
# print(mod2)
# digit = 123
# mod3 = digit%10
# print(mod3)
# digit = 12
# mod4 = digit%10
# print(mod4)
# digit = 1
# mod5 = digit%10
# print(mod5)
# print(mod1+mod2+mod3+mod4+mod5)


num = int(input("Enter your Number\n"))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num //= 10  # num = int(num /10)

print(sum)


# def sayHello():
#     print("Hello")
#
# sayHello()
#
#
# def funcWithParam(a):
#     return a**2
#
# o = funcWithParam(2)
# print(o)

# Lambda Expression -> Now copied by the Java


# def doubleOfMe(value):
#     return value*2


output = lambda value:value*2
print(output(2))


def sayHello(name):
    print("Hi your name is ",name)


sayHelloLambda = lambda name: print("Hi your name is ", name)

sayHello("Pramod")

sayHelloLambda("Lucky")


original_str = "Pramod"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("Pramod") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")



add = lambda x,y : x+y

print(add(3,4))



def funcWithParam(a):
    return a**2


output = funcWithParam(2)
print(output)

