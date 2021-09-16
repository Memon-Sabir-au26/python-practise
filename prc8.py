# Write a program to find second biggest number out of three positive numbers, given by user

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

if (a > b and a < c) or (a > c and a < b):
    print("The 2nd greatest number is 1st number : ", a)

if (b > a and b < c) or (b > c and b < a):
    print("The 2nd greatest number is 2nd number : ", b)

if (c > b and c < a) or (c > a and c < b):
    print("The 2nd greatest number is 3rd number : ", c)
