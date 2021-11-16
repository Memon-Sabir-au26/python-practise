#creating a tuplpe
t=(1,2,3,4,5)
print(t)

#accessing a tuple
print(t[1])

#reverse the tuple
print(t[::-1])

#updating of a tuple 1st method.
u=list(t)
u.append(6)
t=tuple(u)
print(t)

#updating of a tuple 2nd method.
w = t + (7,8,9,10,6,6)
print(w)

print(w.count(6))

print(w.index(5))
#delete a tuple
del w
print(w)


