"""
# Escape Sequence
# special combinations of characters

print("This is a backslash \\")
print("She said: \"Hello, world!\"")
print("This is a new line \nThis is the second line")

# /n Not  \n
print("This is a tab\tThis is after the tab")

# Create a program, take 5 numbers from the user, add 1-2 duplicates
# print the non-duplicate numbers
# Method - 1
a = int(input('enter your number\n'))
b = int(input('enter your number\n'))
c = int(input('enter your number\n'))
d = int(input('enter your number\n'))
e = int(input('enter your number\n'))
my_list = [a,b,c,d,e]
print(set(my_list))

# Method 2
c = []
for a in range(1,6):
    a=int(input("Enter your number:\t"))
    c.append(a)
print("output =",(set(c)))
"""



