# Write a program to print truth table of OR logical operator

"""
The truth table of OR logical operator is :

X   Y   result
T   T     T
T   F     T
F   T     T
F   F     F

This above table is for condition check the program will work as per above table or not
"""

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))

if a==b or c==d :
    print(" x   Y =  Result ")
    print(" T   T =     T ")
    print(" T   F =     T ")
    print(" F   T =     T ")
    print(" F   F =     F ")
    print("The Result of this OR operator is : ")
    print(" T   T =     T ")

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))

if a==b or c!=d :
    print(" x   Y =  Result ")
    print(" T   T =     T ")
    print(" T   F =     T ")
    print(" F   T =     T ")
    print(" F   F =     F ")
    print("The Result of this OR operator is : ")
    print(" T   F =     T ")

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))
    
if a!=b or c==d :
    print(" x   Y =  Result ")
    print(" T   T =     T ")
    print(" T   F =     T ")
    print(" F   T =     T ")
    print(" F   F =     F ")
    print("The Result of this OR operator is : ")
    print(" F   T =     T ")

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))

if a!=b or c!=d :
    print(" x   Y =  Result ")
    print(" T   T =     T ")
    print(" T   F =     T ")
    print(" F   T =     T ")
    print(" F   F =     F ")
    print("The Result of this OR operator is : ")
    print(" F   F =     F ")
