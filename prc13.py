# Q1. What will be the output ? 

i = 2
p = 1

while i <= 10 :
    p = p*i
    i =  i + 1
    print(p)

"""
Output :-
2
6
24
120
720
5040
40320
362880
3628800
"""

# Q2. What will be the output ? 

Sum1 = 0
Sum2 = 0
i = 1

while i < 10 :
    if i%2 == 0 :
       Sum1 = sum1 + i

    else :
       Sum2 = sum2 + i

i = i + 1   
print(Sum1,Sum2)

"""
Output :-
NameError: name 'sum2' is not defined
"""

# Q3. Print the product of first 10 even numbers.

a = 1 
b = 20

for num in range(a, b + 1):
	if num % 2 == 0:
		print(num, end = " ")
