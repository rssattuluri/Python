# File Handling
# How to Read a Text, and Write into it using python Code

# Open a File
# file_object = open("pramod.text", mode)

# Modes:
# 'r' for reading (default).
# 'w' for writing (creates a new file or truncates an existing one).
# 'a' for appending.
# 'b' for binary mode.
# '+' for updating (reading and writing).

# Read a File
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.

# Write to a File

# Writing String: file_object.write(string)
# Writing Multiple Lines: file_object.writelines(list_of_strings)

# Closing a File
# Syntax: file_object.close()

try:
    with open("TestData2.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print(error)


with open('example.txt', 'a') as file:
    file.write("Hello, world!2")

# with open('read.txt', 'r') as file:
#     content = file.read()
#     print(content)


with open('read.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    # The readline() method reads a single line from the file each time it's called.
    # The readlines() method reads all the lines but in List Format
    for line in lines:
        print(line,end='')

with open('existfie.txt', 'a') as file:
    file.write("\nPandey")

# csv - format
import csv
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0],row[1],row[2],sep='|')


# Using pandas Library
import pandas as pd

df = pd.read_csv('data.csv')
print(df)

import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('mydata.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)


# API Automation in Selenium - 90% Read the file
# 10% update the file

import csv

temp_data = []
id_update = 2
new_age = 26

with open('satish.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

# for row in temp_data:
#     print(row[0])
#     print(row[2])
#     if row[0] == id_update:
#         row[2] = new_age

temp_data[2][2] = 26
print(temp_data)



with open('satish.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)
