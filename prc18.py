# Q1. Count no occurrences of a word in a list, where the word is given by a user.

list1 = [ "hello", "a", "hello", "hi", "hello", "ok", "hello" ]
word =input("Enter a Word : ")
print(list1.count(word))

# Q2.Take input from user items and their quantity. And then print the item with the maximum quantity.

items = []
quantity =[]
n = int(input())
for i in range(n):
    item,q=input().split()
    q=int(q)
    items.append(item)
    quantity.append(q)

max_value = max(quantity)
ans = quantity.index(max_value)
print(items[ans])

# Q.3 Define a method that takes a string as a parameter. Insert all the characters of the string into a list. Convert the entire list into a tuple. Return the tuple from the method and print that.

def convert(s):
    lst=list(s)
    tp=tuple(lst)
    return tp

print(convert("Sabir"))


