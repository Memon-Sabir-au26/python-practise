n=5
for k in range(1,5):
    for l in range(1,k+1):
        print("*",end=" ")
    # print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=5
for k in range(1,5):
    for l in range(1,k+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

num = int(input("enter the number of row : "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

num = int(input("enter the number of row : "))
for i in range(num+1,0,-1):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(0,i-1):
        print("*",end=" ")
    print()
