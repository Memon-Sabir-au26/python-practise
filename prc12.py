"""
FizzBuzz - take n as input from the user, From 1 to n, print Fizz if a number is divisible by 3,
print Fuzz if a number is divisible by 5.
print FizzFuzz if a number is divisible by 3 and 5 both

"""

n = int(input("Enter a Number : "))
for i in range(1,n+1):
    if (n % 3 == 0 and n % 5 == 0):
         print ("Fizz-Buzz")
    else:
        if (n % 5 == 0):
            print ("Fuzz")
        if (n % 3 == 0):
            print ("Fizz")
