numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# num%2==0
# even_numbers = [2, 4, 6, 8, 10]


# filter -> Number element can be less or equal the list

def is_even(num):
    return num % 2 == 0


# Mod
# 2| 10 | 5
#    10
#    ---
#    0

even_numbers = filter(is_even, numbers)
print(even_numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)

numbers = [1, -2, -3, -4, 5, 16, -7, 8, -9, -10]


def is_positive(num):
    return num > 0


pos_numbers = filter(is_positive, numbers)
print(pos_numbers)
pov_numbers_list = list(pos_numbers)
print(pov_numbers_list)


words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6


def check_len(w):
    return len(w) >= min_len


op = list(filter(check_len, words))
print(op)


products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]

print(type(products))
print(type(products[0]))

#products[0] - name, price



def is_affordable(pramod):
    return pramod["price"] < 500

def is_affordable_name(pramod):
    return len(pramod["name"]) > 6

affordable_items_price = list(filter(is_affordable,products))
affordable_items_names = list(filter(is_affordable_name,products))
for i in affordable_items_price:
    print(i["price"],i["name"])


for i in affordable_items_names:
    print(i["price"],i["name"])

i = 10
name = "pramod"
print(i)
print(name)
print(name+str(i))
# print(int(name)+i)


numList = [30, 2, -15, 17, 9, 100]
list_of_numbers_grater_10 = list(filter(lambda sik: sik > 10, numList))
print(list_of_numbers_grater_10)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def is_even(num):
    return num % 2 == 0


even_numbers_tuple = tuple(filter(is_even, numbers_tuple))
print(even_numbers_tuple)

l = [(1, 23), (34, 34)]
print(l)
print(l[0])
print(l[0][0])
print(l[0][1])









