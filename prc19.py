# Q1. Write a program to find the count of all even no’s and odd no’s in an array / list.





list1 = [1,2,3,4,5,6,7,8,9,10]
n = len(list1)

def EvenOdd(list1, list1_size):
    even_count = 0
    odd_count = 0

    for i in range(list1_size):
    
        if (list1[i] & 1 == 1):
            odd_count = odd_count + 1
        else:
            even_count = even_count + 1
 
    print("Odd_count = ",odd_count)

    print("Even_count = ",even_count)
          
EvenOdd(list1, n)

# Q2. Write a program to create a dictionary for above program.

list1 = [1,2,3,4,5,6,7,8,9,10]
n = len(list1)

def EvenOdd(list1, list1_size):
    even_count = 0
    odd_count = 0

    for i in range(list1_size):
    
        if (list1[i] & 1 == 1):
            odd_count = odd_count + 1
        else:
            even_count = even_count + 1
 
    print("Odd_count = ",odd_count)

    print("Even_count = ",even_count)

mydict = {}
mydict["Odd_count"] = 5
mydict["Even_count"] = 5
print(mydict)

#Q3. Write a program to find the count of every vowel in a string

a_string = "envelope "
lowercase = a_string.lower()

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count

print(vowel_counts)
