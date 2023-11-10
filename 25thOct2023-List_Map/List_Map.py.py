# List - Collection of Items( Duplicate is allowed)
my_list = [1, 2, 3]
my_list2 = [1, True, "Pramod", 12.34]

print("Initial list:", my_list)

# Indexing
print("Element at index 0:", my_list[0])

# Changing an element
my_list[1] = 20
print("List after changing element at index 1:", my_list)

# append()
my_list.append(4)
print("List after appending:", my_list)

# extend()
my_list.extend([5, 6])
print("List after extending:", my_list)

# insert()
my_list.insert(1, 'a')
print("List after inserting 'a' at index 1:", my_list)

# remove()
my_list.remove('a')
print("List after removing 'a':", my_list)

# clear()
my_copy_list = my_list.copy()
print(my_copy_list)

my_list.clear()
print("Initial list:", my_list)

print(my_copy_list)
# index()
# print("Index of 3 in the list:", my_list.index(3))

my_copy_list.sort()
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])


print(len(my_copy_list))

my_list = my_copy_list.copy()
print(my_list.remove(4))



my_list = [True, "Pramod", 12.34, 90]
my_list.sort() # TypeError: '<' not supported between instances of 'str' and 'bool'
print(my_list)


squares = [1, 4, 9, 16, 25]
l = squares
l2 = squares.copy()
# print(squares)
# print(l)
# print(l2)
squares[0] = 33

print(squares)
print(l)
print(l2)


squares = [1, 4, 9, 16, 25, 1]
# index = [0, 1, 2, 3, 4]
# rev_index = [-5, -4, -3, -2, -1]
print(squares[0])
print(len(squares))
print(squares.count(1))
print(squares[-1])

# Real LIVE
# List of Web Elements

# element1 = driver.findElement("email")
# element2 = driver.findElement("password")
# element3 = driver.findElement("submit")
#
# list_element = [element1,element2,element3]
# list_element[0].click()


squares = [1, 4, 9, 16, 25, 1]  # List - This allow Duplicate
print(type(squares))
squares_tuple = (1, 4, 9, 16, 25, 1)
print(type(squares_tuple ))


list = []
if not list:
    print("Empty")
else:
    print("Not Empty")
    

squares = [1, 4, 9, 16, 25]
# index = [0, 1, 2, 3, 4, 5]
# print(squares.pop(1)) # Pop will remove the index value
print(squares)
# print(squares.remove(1)) # Remove the Value not the Index
print(squares.pop(1)) # Remove the Value not the Index
print(squares.remove())



test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))



print("12")
print(type("12"))
a = "12"
c = 12.34
b = int(a)
d = int(c)
print(type(a))
print(type(c))
print(type(b))
print(type(d))

t = True # 1, False  0
print(int(t))


st = "pramod"
my_list =  list(st)
print(my_list)
my_list.sort()
print(my_list)


l = [1, 12.34, "Pramod"]
my_int = int(l[2])
print(my_int)


list = [1,4,9,16]
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort


# Map and Filter in the List


# Map Functions ( where we will go from one item and apply a functions)
numbers = [1, 2, 3, 4, 5]
# sq_numbers = [1, 4, 9, 16, 25]
sq = lambda x: x * x
sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)


def ThreeTimes(a):
    return a ** 3


# Map Function
sq_numbers3 = list(map(lambda x: x * 3, numbers))
sq_numbers2 = list(map(ThreeTimes, numbers))
print(sq_numbers2)
print(sq_numbers3)






