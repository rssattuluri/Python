"""
# f-strings in python
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

#string formatting
name="Ramya"
age=32
#f-strings
print(f"My name is {name} and I am {age} years old")
#str.format
print("My name is {} and I am {} years old.".format(name,age))

#str(int_value)
#example
a=str(20)
print(type(a))

#str(float_value)
b= str(34.8)
print(type(b))

s = "Ramya Is A Good Tester"
#Searching for substrings:
print(s.endswith("Tester"))
print(s.startswith("hyma"))      # Checks if the string starts with a specified prefix.
print(s.startswith("chaitra"))  #  Checks if the string ends with a specified suffix.
#str.find(substring)            #Searches for a substring and returns the index of its first occurrence (or -1 if not found).
print(s.find("bad"))     # -1 (if not fount string)
print(s.find("Good"))     # returns 10 (Searches the string for a specified value and returns the last position of where it was found)
print(s.count("a"))
print(s.strip())	      #Removes leading and trailing whitespace characters.
print(s.split())	      #Splits a string into a list of substrings based on whitespace by default (can specify a separator).

#Task3:list of all functions for the string data types
s = "Ramya Is A Good Tester"
print(len(s))
print(type(s))

#Testing strings:
print(s.isalnum())	   #Checks if all characters in the string are alphanumeric.
print(s.isalpha())	   #Checks if all characters in the string are alphabetic.
print(s.isascii())	   #Returns True if all characters in the string are ascii characters
print(s.isdecimal())   #Returns True if all characters in the string are decimals
print(s.isdigit())	   #Checks if all characters in the string are digits.
print(s.isidentifier()) #Returns True if the string is an identifier
print(s.islower())	    #Returns True if all characters in the string are lower case
print(s.isnumeric())     #Returns True if all characters in the string are numeric
print(s.isprintable())   #Returns True if all characters in the string are printable
print(s.isspace())	    #Returns True if all characters in the string are whitespaces
print(s.istitle())	   #Returns True if the string follows the rules of a title
print(s.isupper())	   #Returns True if all characters in the string are upper case

#Searching for substrings:
s = " Ramya Is A Good Tester "
print(s.endswith("Tester"))
print(s.startswith("Swetha"))      # Checks if the string starts with a specified prefix.
print(s.startswith("Ramya"))  #  Checks if the string ends with a specified suffix.
#str.find(substring)            #Searches for a substring and returns the index of its first occurrence (or -1 if not found).
print(s.find("bad"))     # -1 (if not fount string)
print(s.find("Tester"))     # returns 10 (Searches the string for a specified value and returns the last position of where it was found)
print(s.count("a"))
print(s.strip())	      #Removes leading and trailing whitespace characters.
print(s.split())	      #Splits a string into a list of substrings based on whitespace by default (can specify a separator).

#Converting strings:
s = "Ramya Is A Good Tester"
print(s.capitalize())        #Capitalizes the first character of the string.
print(s.title())            #Capitalizes the first character of each word in the string.
print(s.lower())            #Converts all characters in a string to lowercase.
print(s.upper())            # Converts all characters in a string to uppercase.
print(s.swapcase())         #Swaps the case of characters (Exapmle:uppercase to lowercase and vice versa).
#print(s.replace("old","new")) #Replaces occurrences of a substring with another substring.
print(s.replace("Good","Excellent"))

#Task2:Take a user from input and print a table
n = int(input("Enter a number: "))
print(f"table of {n} is:")

print(f'{n} x 1 = {n*1}')
print(f'{n} x 2 = {n*2}')
print(f'{n} x 3 = {n*3}')
print(f'{n} x 4 = {n*4}')
print(f'{n} x 5 = {n*5}')
print(f'{n} x 6 = {n*6}')
print(f'{n} x 7 = {n*7}')
print(f'{n} x 8 = {n*8}')
print(f'{n} x 9 = {n*9}')
print(f'{n} x 10 = {n*10}')

#using for loop
n=int(input("Enter the number to print the table for: "))
for i in range(1,11,1): # range takes start value, stop value(-1) and increment value
    print(n,"x",i,"=",n*i)

# 4th Oct Home work
name=input("enter your name: ")
print(name,"welcome to the python class")

first_name=input("enter first name:\t")
second_name=input("Enter second name:\t")
print(first_name,second_name,sep="-")
print(first_name,second_name,"welcome to the python class")

name=input("Enter user name: ")
print("Ramya","Swetha",sep="-",end="\t") # \t - tab (one space)

import keyword
print(keyword.kwlist) # List of keywords which cannot be used for assigning variables as they are reserved
"""


