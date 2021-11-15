#list syntax
f = [1,2,3,4,5]
print(f)

#lenght of the list
print(len(f))

#access the list
print(f[1])
# here 1 is index value and its value is 2.

#slicing the list
print(f[1:5])
#same here 1 and 5 are index value for slicing last index should be n-1.

#reverse the list
print(f[::-1])

#append the list 
f.append(7)
print(f)
#it will add element in the last of the list.

#insert the element in the list
f.insert(5,6)
print(f)

#remove the element from the list
f.remove(7)
print(f)
#here 7 is value not index no.

#pop is using for removing element using index value.
f.pop(5)
print(f)

#blank pop remove the last value of the list.
f.pop()
print(f)

#update the list.
f[3] = 5
print(f)

#extend the list or joining 2 list.
g = [6,7,8,9]
f.extend(g)
print(f)

#clear the list.
f.clear()
print(f)