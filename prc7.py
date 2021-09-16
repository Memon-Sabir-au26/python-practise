# Write a program to find biggest number out of three positive numbers, given by user.

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))

if a > b > c :
    print("The greatest number is 1st number : ", a)

elif b > a > c :
    print("The greatest number is 2nd number : ", b)
    
else :
    print("The greatest number is 3rd number : ", c)
    