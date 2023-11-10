scale = int(input("Enter the num\n"))
if scale >= 90 and scale <= 100:
    print("grade is A")
elif scale >= 80 and scale <= 89:
    print("grade is B")
elif scale >= 70 and scale <= 79:
    print("grade is C")
elif scale >= 60 and scale <= 69:
    print("grade is D")
elif scale >= 0 and scale <= 59:
    print("grade is F")
else:
    print("invalid input")


year = 2024
is_leap_year = False

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True

print(f"{year} is {is_leap_year}")

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Eq")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Iso")
else:
    print("Scalene")


# Break and Continue with the Loops

# Break
# 1 to 10 -> break when value of count = 5 -> 1,2,3,4,5,x
# put the debug point when you see condition
# count = 1
# while count <= 10:
#     print(count)
#     if count >= 5:
#         break
#     count = count + 1

# I want to break when count = 5

for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)
print("For loop is finished")


# Continue

for num in range(1, 10):
    if num % 2 == 0:
        print("Found even Number", num)
        print(f"Found even Number {num}")
        continue
    print("Odd number Found", num)


for i in range(1,10):
    if i == 5:
        pass
    else:
        print(i)


# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

#Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13