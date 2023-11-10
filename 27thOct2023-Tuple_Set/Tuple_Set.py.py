# List is Mutable, Its content can be changed!
my_list = [1, 2, 3, 4, 5, 5]
print(my_list)
my_list[1] = 20
print(my_list)
print(type(my_list))

# Tuple - It is immutable in nature. - No modification
car = ("Ford GT", "Raptor", "Lambo", "Lambo")
car2 = ("Ford GT", True, "Lambo")
print(car)
print(type(car))
# car[1] = "XUV 500"

print(len(car))

# Tuple (), Its content can't be changed, List [] and it content can be changed!

# List can be converted

list1 = [1, 2, 3, 4, 5, 6]
print(tuple(list1))


tuple1 = ()
tuple2 = (1, 2, 3, 4, 5)
tuple3 = tuple(["Pramod", "Lucky"])
print(tuple1)
print(tuple2)
print(tuple3)

del tuple3
print(tuple3)

tuple3 = tuple(["Pramod", "Lucky"])
print(tuple3)
print(tuple3[0])
print(tuple3[1])

# Merging Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

# Convert to List
my_tuple = (1, 2, 3, 4, 5)
print(list(my_tuple))

x = 10
a, b = 23, 34  # This is multiple value assign
q, w, e = (45, 56, 78)  # tuple assigned to multiple variables
print(q)
print(w)
print(e)


# Nested Tuples

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)
print(len(awesome_team))
print(awesome_team[0])
print(awesome_team[1])


print(awesome_team[0][1]) # Bruce
print(awesome_team[1][1]) # Diana Prince


# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("Moscow" in cities)


# String
name = "Pramod"
name[0] = "A"
print(name)

# String vs Tuple
# String is bunch of character
# tuple is list of any data type items which can't changed.
# list is collection of items, which can be changed, you can duplicated

list = [1,2,3]
tup = (1,2,3)
string = "pramod"


# Set -

# Initial Blank Set
set1 = set()
print(set1)

set2 = set("Pramod")
print(set2)

set3 = {1, 2, 3, 4, 5, 5, 4}
print(set3)
print(type(set3))

# List of element - in Web Automation
# Can  set to store the value, so that we don't have duplicate!!


set3 = {1, 2, 3, 4, 5, 5, 4}
#set3[1] = 34 # Not possible!, Immutable?
print(set3)

set1 = set(["Pramod", "For", "Pramod"])
print(set1)



# List
list1 = [45.2, 33, 33, 45, 21]
print(len(list1))

# Print Unique Items
set1 = set(list1)
print(set1)


t=("TheTestingAcademy","for","TheTestingAcademy")
print("\nSet with the use of Tuple: ")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.difference(set2)
my_set2 = set2.difference(set1)
print(my_set)
print(my_set2)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# l3 = l1



set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)

for i in set1:
	print(i)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])


set1.remove(5)
set1.remove(6)
print(set1)


def func():
    name = "Pramod"
    return name

def func2():
    name = "Pramod"
    name

# Is this function return anything?

# output = func()
output = func2()
print(output)

num = 20

def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n


op = multiply_by_10(num)
print(op)
print("Value of num outside function:", num)

list1 = [10, 20, 30, 40]
tuple1 = (10, 20, 30, 40)
print(list1)


def mul_by10(a):
    a[0] *=10
    a[1] *=10
    a[2] *=10
    a[3] *=10


print(list1)
mul_by10(list1)
mul_by10(tuple1)
print(list1)
print(tuple1)

def sayHello():
    print("Hello")


sayHello()

op = sayHello()
print(op)


a = max(45,33,3)
print(a)