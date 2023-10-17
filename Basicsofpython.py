#  print("Hello World")
"""
a = int(input("Enter your number"))
b = int(input("Enter your number"))

c = a + b
print(c,type(c))

Arithmetic operators
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10**3)
print(10//3)
print(10%3)

#list
a = [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]
print(a)            # prints whole List
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;
print(a[-2:-1])      # start index : end before index;
print(a[4:])        # start index : till end of List;
print(a[:9])        # from start of List: end before index
print(a[:])         # from start of List: till end of List
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of List: till end of List: jump
print(a[::-1])      # reversing a List using jump as -1

print([1,2,3] + [33,44,55])
print([1,2,3] * 3)


a = [1,22,3.4,True,'hello',3.4]
a.append(100)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.pop()
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.pop(0)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.insert(0,122)     #(position,value)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.remove(1)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.remove(22)
print(a)

a = [1,22,3.4,True,'hello',3.4]
a.clear()   #(position,value)
print(a)

a = [1,22,3.4,True,'hello',3.4]
x = a.index(22)
print(x)

a = [1,22,3.4,True,'hello',3.4]
x = a.index(222)
print(x)

a = [1,22,3.4,True,'hello',3.4,1,1,1,1,1,1]
x = a.count(1)
print(x)

a = [1,22,3.4,True,'hello',3.4,1,1,1,1,1,1]
x = a.count(0)
print(x)

a = [1,22,3.43,1,1,1,1,1,1]
a.sort()
print(a)

a = [1,22,3.43,1,81,17,14,1,21]
a.reverse()
print(a)

a = [1,22,3.43,1,81,17,14,1,21]
a.sort()
a.reverse()
print(a)

a = [1,22,3.43,1,81,17,14,1,21]
b = [111,222,333]
a.extend(b)
print(a)
print(b)

a = [1,22,3.43,1,81,17,14,1,21]
b = (111,222,333)   # Its a tuple
a.extend(b)
print(a)
print(b)

#Tuple
a = (1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33)
print(a)            # prints whole Tuple
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index;
print(a[3:-1])      # start index : end before index;
print(a[4:])        # start index : till end of Tuple;
print(a[:9])        # from start of Tuple: end before index
print(a[:])         # from start of Tuple: till end of Tuple
print(a[0:11:2])    # start index : end before index : jump
print(a[::3])       # from start of Tuple: till end of Tuple: jump
print(a[::-1])      # reversing a Tuple using jump as -1

a = (1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33)
print(a)
x = a[::-1] # Stores a newly created tuple in 'x' variable
print(x)

a = (1,22,3.4,True,'hello',3.4)
x = a.index(22)
print(x)

a = [1,22,3.4,True,'hello',3.4]
x = a.index(222)
print(x)

a = (1,22,3.4,True,'hello',3.4,1,1,1,1,1,1)
x = a.count(1)
print(x)

a = [1,22,3.4,True,'hello',3.4,1,1,1,1,1,1]
x = a.count(909)
print(x)

#Dictionary
a = {100:8, 'apple':2, 55.5:45, 2:782, 6:3, 6:9, 6:20}
x = a.values()
print(x)

a = {100:8, 'apple':2, 55.5:45, 2:782, 6:3, 6:9, 6:20}
x = a.keys()
print(x)

a = {100:8, 'apple':2, 55.5:45, 2:782, 6:3, 6:9, 6:20}
x = a.items()
print(x)

a = {100:8, 'apple':2, 55.5:45, 2:782, 6:3, 6:9, 6:20}
a.clear()
print(a)

a = {100:8, 'apple':2, 55.5:45, 2:782, 6:3, 6:9, 6:20}
a.popitem()
print(a)

a = {10:1, 20:2, 30:3}
b = {40:4, 50:5, 10:100}
print(a.keys())
print(b.values())

#Set
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))

a = {1,2,3,4,5}
b = {4,5,6,7,8}
x = a.intersection(b)
print(x)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
x = a.difference(b)
print(x)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
x = b.difference(a)
print(x)

#String
a = "helloworld"
print(a)            # prints whole string
print(a[7])         # access the positive Index
print(a[-2])        # access the negative Index
print(a[1:9])       # start index : end before index (1-8)
print(a[3:-1])      # start index : end before index (3-8)
print(a[4:])        # start index : till end of string
print(a[:9])        # from start of string : end before index
print(a[:])         # from start of string : till end of string
print(a[0:10:2])    # start index : end before index : jump (0-9)
print(a[::3])       # from start of string : till end of string : jump
print(a[::-1])      # reversing a string using jump as -1

a = 'hello world'
x = a.isalpha()
print(x)

a = 'helloworld'
x = a.isalpha()
print(x)

a = '1234'
x = a.isalpha()
print(x)

a = '1234'
x = a.isdigit()
print(x)

a = '1234hello'
x = a.isdigit()
print(x)

a = '12 34'
x = a.isdigit()
print(x)

a = '1234'
x = a.isalnum()
print(x)

a = 'abcd'
x = a.isalnum()
print(x)

a = 'abcd1234'
x = a.isalnum()
print(x)

a = "abcd 1234"
x = a.isalnum()
print(x)

a = 'HELLO WORLD'
x = a.lower()
print(x)

a = 'Hello world'
print(a.upper())

a = 'HELLO WORLD'
x = a.upper()
print(x)

a = 'Hello world'
x = a.title()
print(x)

a = 'HELLO WORLD Its a Great Day'
x = a.title()
print(x)

a = "Hello Sun ITS a good day"
x = a.swapcase()
print(x)

a = "HEllo woRLD"
x = a.swapcase()
print(x)

a = "Hello Sun ITS a good day"
x = a.split(' ')
print(x)

a = "HEllo woRLD"
x = a.split('o')
print(x)

a = ["hello", "world", "Iam", "fine"]
x = "+*+".join(a)
print(x)

a = ["hello", "world", "have", "a", 'Great', 'Day']
x = "_".join(a)
print(x)

a = "hello world iam china igloo"
x = a.replace('o','*')
print(x)

a = "hello world iam china igloo"
x = a.replace(' ','_')
print(x)

a = "The quick brown fox jumps over the lazy dog idiom"
x = a.count('i')
print(x)

a = "The quick brown fox jumps over the lazy dog idiom"
print(a.count("z"))

a = "The quick brown fox jumps over the dog idiom"
x = a.find('z')
print(x)

a = "The quick brown fox jumps over the dog idiom"
x = a.index('q')
print(x)

a = "The quick brown fox jumps over the dog idiom"
x = a.index('b')
print(x)

a = 'Mithran'
b = 'Green'
c = 'Black'
mystr = "Hello {}, {} bike, {} car"

x = mystr.format(a,b,c)
print(x)

a = 'Green'
b = 'Black'
mystr = "Colours = {},{},Red"

x = mystr.format(a,b)
print(x)
"""

def myfun():
    print("Hello Ramya")
