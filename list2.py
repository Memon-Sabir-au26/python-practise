"""
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.
"""

def swaplist(newlist):
    newlist[0] , newlist[-1] = newlist[-1] , newlist[0] 
    return newlist

newlist = [12,35,9,56,24]
print()
print("the list is : ",end= " ")
print(newlist)
print()
print("after swapping the list :",end=" ")
print(swaplist(newlist))
print()

def swaplist(list):
    list[0],list[-1] = list[-1],list[0]
    return list

list = [1,2,3,4,5]

print(swaplist(list))

"""
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
"""

list = [23,65,19,90]
def swaplist(list):
    list[0],list[2] = list[2],list[0]
    return list

print(list)
print(swaplist(list))

"""
input : ['Gfg', 'is', 'best', 'for', 'Geeks']
output : ['efg', 'is', 'bGst', 'for', 'eGGks']
"""
list = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(list)

res =[sub.replace('G','-').replace('e','G').replace('-','e') for sub in list]
print(res)

list = ["sabir","junaid","arzoo","halim","saad"]
print(list)

res = [sub.replace("sabir","sabir-smarty").replace("junaid","junaid-chu").replace("arzoo","arzoo-rotdu").replace("halim","halim-chammad").replace("saad","saad-the-hippo") for sub in list]
print(res)

"""
The list is : [1, 4, 5, 7, 8]
Length of list using naive method is : 5
"""

list = [1,4,5,7,8]
print(list)
count = 0
for i in list:
    count = count + 1
print(count)

list = [1,2,3,4,5]
print(list)
print(len(list))

"""
Input: a = 2, b = 4
Output: 4

"""

a = 2
b = 4
if a > b :
    print(a)
else :    
    print(b)


def maxnum(a,b):
    if a > b :
        return a
    else :
        return b

a = 2
b = 4
print(maxnum(a,b))


"""
Input: a = 2, b = 4
Output: 2

"""

a = 2
b = 4
if a < b :
    print(a)
else :    
    print(b)


def maxnum(a,b):
    if a < b :
        return a
    else :
        return b

a = 2
b = 4
print(maxnum(a,b))

"""
Checking if 4 exists in list ( using loop ) : 
Element Exists
Checking if 4 exists in list ( using in ) : 
Element Exists
"""

list = [1,2,3,4,5]

for i in list:
    if(4==i):
        print("search element is exist in list")


list = [1,2,2,3,2,2,4,5,6,7,8,9,10]
n = int(input("Enter the Element for search : "))
check = list.count(n)
if check > 0 :
    print(n,"Elemnt Exists in the list ",check,"times !!!")
else :
    print(n,"Elemnt Does Not Exists !!!")

"""
Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]
"""

list = [10, 11, 12, 13, 14, 15]
print(list)
print(list[::-1])

def reverselist(list):
    list.reverse()
    return list

list = [1,2,3,4,5]
print(list)
print(reverselist(list))

def copylist(list1):
    list2 = list1
    return list2

list1 = [1,2,3,4,5]
list2 = copylist(list1)

print(list1)
print("after printing" ,list2)

list1 =[1,2,3,4,5]
copylist = []
copylist.extend(list1)
print(copylist)