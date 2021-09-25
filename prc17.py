# Q1. Write a program to take input from the user and make a list of integers.

list1=[]
def insert_element():
    element = int(input("Enter Value : "))
    list1.append(element)
    print(list1)
    insert_element()

insert_element()

# Q2. Write a program to convert above list to a tuple.

list2=[ 1, 2, 3, 4, 5]
print(tuple(list2))

# Write a program to remove the 4th last element from a list, and put a string before the 2nd last element.

list3=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
list3.pop(-4)
list3.insert(-2,"sabir")
print(list3)