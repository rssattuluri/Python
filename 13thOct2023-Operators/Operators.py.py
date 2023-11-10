#  Arithmetic Operators:
# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Modulus (remainder)
# ** Exponentiation
# // Floor division (returns the quotient, discarding the remainder)


# can we take the value from user?
a = int(input("Enter the value of a\n")) # 10
b = int(input("Enter the value of b\n")) # 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) #10^3
print(a//b) # 10/3 0 -> 3.3 -> int -> 3 Q
print(a%b)

# Comparison Operators:
# == Equal to
# != Not equal to
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to

x = 5
y = 10

print(x == y)  # bool -> False or false ?
print(x != y)
print(x > y)
print(y > x)
print(x <= y)
print(x >= y)

x = 5
y = 5
print( x >=y) # 5 > 5 or 5== 5 ->  True
# A B O ( 0 - False, 1 - True)
#  0 0 0
#  0 1 1
#  1 0 1
#  1 1 1

#Logical Operators:
# and Logical AND
# or Logical OR
# not Logical NOT

p = True
q = False
print(p and q)
print(q or p)

print(not p)

# Assignment Operators:
# = Assignment
# += Add and assign
# -= Subtract and assign
# *= Multiply and assign
# /= Divide and assign
# %= Modulus and assign
# **= Exponentiate and assign
# //= Floor divide and assign

a = 5
a+=2 # a = a+2 increase by 2
print(a)

a-=1 # a= a-1
print(a)
a*=3 # a = a*3
print(a) # 18

a/=2 # 9
print(a) # 9
a%=4  # 9%4 -> 1
print(a)

# Membership Operators:
# in Returns True if a value is found in the sequence
# not in Returns True if a value is not found in the sequence

my_list = [1,2,3,3,54]
print(54 in my_list) # True or False ->  True we found the element in the list
print(53 in my_list)
print(53 not in my_list)

#Identity Operators:
# is Returns True if both variables are the same object
# is not Returns True if both variables are not the same object

# x = #Identity Operators:
# is Returns True if both variables are the same object
# is not Returns True if both variables are not the same object

x = [1,2,3]
y = [1,2,3]


print(x is y)
print(id(x))
print(id(y))

print(x is y)
print(x is not y)
print(id(x))
print(id(y))

a = 10
print(+a)
print(-a)

a = 5  # binary: 101
print(~a)

# if else
# age > 18 ->  watch a movie
# age < 18 -> not alglowd to watch movie

# Ternary Operator

# result_if_true if condition else result if_false
x = 5
y = 10

max_val = x if x >y else y
print(max_val)

age = input("Enter your age\n")
age = int(age)

result  = "Yes" if age > 18 else "No"
print(result)


