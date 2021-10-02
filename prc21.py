"""
Q1. Create a Student class with a parameterized constructor having parameters:
1.	Name
2.	Roll
3.	Batch 
4.	Institute = “AttainuU”

Name, Roll and Batch should be instance attribute where as Institute should be a class attribute.

Create three objects with the following data:
Object1 : “Abdul” , 1, “Bhabha”.
Object2 : “Ram”, 2, “C V Raman”.
Object3:  “Shyam”, 4, “Einstein”
 
Define a method show inside the same class which prints all the data of an object.

"""
class student:

    Institute = "AttainuU"

    def __init__(self, name, rollno, batch):
        self.studentname = name
        self.studentrollno = rollno
        self.studentbatch = batch

    def show(self):
        print(self.studentname)
        print(self.studentrollno)
        print(self.studentbatch)

object1 = student("Abdul", 1, "Bhabha")
object2 = student("Ram", 2, "C V Raman")
object3 = student("Shyam", 4, "Einstein")
object1.show()
object2.show()
object3.show()
