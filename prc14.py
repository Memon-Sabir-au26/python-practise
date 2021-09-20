"""
Write the program to print the pattern :
1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1

"""

n = 5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

"""
Write the program to print the pattern :
*
* *
* * *
* * * *
* * * * *

"""

n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print(" *",end="")
    print()
