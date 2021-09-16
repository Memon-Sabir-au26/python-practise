""" FizzBuzz -
if a number is divisible by 3 - print Fizz,
if a number is divisible by 5 - print Fuzz,
if a number is divisible by both - print Fizz-Buzz. """

a = int(input("Enter the number : "))

if (a % 3 == 0 and a % 5 == 0):
     print ("Fizz-Buzz")
else:
 if (a % 5 == 0):
    print ("Fuzz")
 if (a % 3 == 0):
     print ("Fizz")
