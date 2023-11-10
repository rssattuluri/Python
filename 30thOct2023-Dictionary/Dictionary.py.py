# Dictionary in Python
# Key and Value Pair

name = "Pramod"
# Key -> name
# Value - Pramod

# A dictionary is an unordered collection of data in a key-value pair format.
# It is defined using curly braces {} and consists of keys and their associated values.

#set -> values  , pramod, lucky, unique values
#dic key and values  name -> pramod

my_dict  = {}
my_dict2 = dict()

print(type(my_dict))
print(type(my_dict2))


phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}

# Dict ?  It is very close to the JSON
print(phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])

# You can access element by Key only - Dict


phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

pramod_details = dict(name="Pramod", age=34, isMale=True, Address="KA")
pramod_details2 = {"name": "Pramod", "90": 34.34, "isMale": True, "Address": "KA"}
print(pramod_details)
print(pramod_details['age'])
print(pramod_details.get('age'))
# print(pramod_details2['age'])

print(pramod_details2.get(90))

print(pramod_details)


# Dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(my_dict)

# If you have a duplicate key, latest value of key will be used!!

keys = my_dict.keys()
values = my_dict.values()

# Get all the keys into a List
keys_list = list(keys)

print(values)

print(keys_list[0])
print(keys_list[1])
print(keys_list[2])



my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}

# Dict - Key and Value

# my_dict.clear()

print(my_dict)

copy_my_dict = my_dict.copy()
print(copy_my_dict)


print(my_dict.items())
set_dic = set(my_dict.items())



my_dict = {'a': 1, 'b': 2}

val = my_dict.pop('a')
print(val)

print(my_dict)

# API Testing -> JSON so we can use Dict which is similar data type as JSON

print(dir(dict()))


# How to Iterate over the Dict?

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k,v)



my_dict = {'a': 1, 'b': 2, 'c': 3}
# val = my_dict.pop('a')
# print(val)


# popitem() is used to remove and return an arbitrary key-value pair (as a tuple)
# from the dictionary.
val = my_dict.popitem()
print(val)
print(my_dict)

del my_dict

print(my_dict)




my_dict = {'b': 2, 'a': 1, 'c': 3}
print(my_dict)
val = my_dict.pop('a')
print(val)
# print(my_dict.pop('b'))
# print(my_dict.pop('c'))
print(my_dict)
my_dict['a'] = val
print(my_dict)


# OrderedDict
# key-value pairs based on the order of insertion

# list, set, tuple, dict, OrderedDict, - API Automation and Selenium

from collections import OrderedDict
od =  OrderedDict()
od['a'] = 45
od['c'] = 78
od['b'] = 97
od['d'] = 31

print(od)

# Selenium - Insert the Web elements into a Dict
# You want to keep the order - login elemtns, dashboard elements,

# Dict - It will not keep the Order of insertion
# OrderedDict - It will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sort=sorted(keys)
print(keys_sort)

keys_sort_rev=sorted(keys, reverse=True)
print(keys_sort_rev)



od2 = OrderedDict()
od2[keys_sort[0]] = 45
od2[keys_sort[1]] = 78
od2[keys_sort[2]] = 89
od2[keys_sort[2]] = 109
print(od2)



# Automation Tester - API and Web Automation
# Python - Vast - Not all the fucntions are required to built your frameworks
# To even crack the Interview

my_dict = {'b': 2, 'a': 1, 'c': 3}
for k, v in my_dict.items():
    if k == 'b':
        print("b is found!!")

op = 'b' in my_dict
op2 = 'd' in my_dict
print(op)
print(op2)

my_dict2 = {True: 123}
print(my_dict2)
print(type(my_dict2))
print(my_dict2[True])


api_response = {
    "first_name": "Pramod",
    "age": 34,
    "last_name": "Dutta",
    "email": "pramoddutta{{$randomInt}}@live.com",
    "password": "Test@4321",
    "commission": 10,
    "roles": [
        4
    ]
}

print(api_response)
print(type(api_response))

print(api_response.get('password'))

print(api_response['roles'])
print(api_response.get('roles'))

api_response['age'] = 43
print(api_response)

for key, value in api_response.items():
    print(key, value)

a = {
    "bookingid": 2384,
    "booking": {
        "firstname": "PRAMOD",
        "lastname": "Dutta",
        "totalprice": 432,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
}

print(a["booking"]["bookingdates"]["checkin"])



my_dict = {}
key = input("Enter a key: ")
value = input("Enter a value: ")
my_dict[key] = value
print("Updated dictionary:", my_dict)