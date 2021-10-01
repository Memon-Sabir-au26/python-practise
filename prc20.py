# Q1. Create a Student class and initialize it with a name and roll number. create an object of that class in the same file and print name and roll number.

class Student:

    StudentName = "Sabir", "Junaid"
    RollNo = 1, 2

attainu = Student()
print("Student names are :",attainu.StudentName)
print("Student roll nos are :",attainu.RollNo)

# Q2. Write the above code to enter details of 10 students, and take input from the user.

class Student:
    
    StudentName = "Sabir", "Junaid"
    RollNo = 1, 2

    def __init__(self):
        for i in range(1,11):
            std_Name = input("Enter name : ")
            Roll_No = input("enter roll no : ")
            print (std_Name)
            print (Roll_No)

attainu = Student()


