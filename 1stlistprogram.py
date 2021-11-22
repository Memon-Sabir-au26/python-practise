# lets start

my_list = []

def listelement():
    print("Welcome !!!!!")
    print("Press 1 for add element in the list")
    print("Press 2 for access the element in the list")
    print("Press 3 for update element in the list")
    print("Press 4 for remove element in the list")
    print("Press 5 for slicing list")
    print("Press 6 for reverse the list")
    print("Press 7 for clear the list")
    print("Press 8 to exit the program")
    print()

    i = int(input("Enter a number from above list to perform a operation : "))

    while i < 9 :
        if i == 1 :
            print("welcome to add session !!!!")
            print("Press 1 for add element in String")
            print("Press 2 for add element in Integer")
            print("Press 1 for add element in Float")
            print("Press 1 for add element in Boolean")
            print("Press 5 for exit")

            insert_input = int(input("Enter a number : "))

            if insert_input == 1 :
                string_input = input("Enter a String : ")
                my_list.append(string_input)
                continue
            
            elif insert_input == 2 :
                integer_input = int(input("Enter a Integer : "))
                my_list.append(integer_input)
                continue
            
            if insert_input == 3 :
                float_input = float(input("Enter a Float : "))
                my_list.append(float_input)
                continue
            
            elif insert_input == 4 :
                boolean_input = bool(input("Enter a Boolean : "))
                my_list.append(integer_input)
                continue

            else:
                print(listelement)
                listelement()

        elif i == 2 :
            print("welcome to access session !!!!")
            print(my_list)
            access_input = int(input("Enter a index number : "))
            print(my_list[access_input])
            listelement()

        elif i == 3 :
            print("welcome to update session !!!!")
            print(my_list)
            update_input = int(input("Enter a index number : "))

            print("Press 1 for update value in Integer ")
            print("Press 2 for update value in String ")
            print("Press 3 for update value in Float ")
            print("Press 4 for update value in Boolean ")

            update_value = int(input("Enter a number : "))

            if update_value == 1 :
                update_string = int(input("Enter integer value : "))
            elif update_value == 2 :
                update_string = input("Enter string value : ")
            elif update_value == 3 :
                update_string = float(input("Enter float value : "))
            elif update_value == 4 :
                update_string = bool(input("Enter boolean value : "))

            my_list[update_input] = update_string
            print("List after update : ",my_list)
            listelement()

        elif i == 4:
            print("welcome to remove session !!!!")
            print(my_list)
            remove_input = int(input("Enter a index number : "))
            my_list.pop(remove_input)
            print("List after removal : ",my_list)
            listelement()

        elif i == 5 :
            print("welcome to slicing session !!!!")
            start_input = int(input("Enter Starting index value : "))
            end_input = int(input("Enter ending index value : "))
            print("Before Slicing : ",my_list)
            print("After Slicing : ",my_list[start_input:end_input])
            listelement()
        
        elif i == 6 :
            print("welcome to reverse session !!!!")
            print("Press 1 for reverse entire list")
            print("Press 2 for modified the and then reverse the list")
            print("Press 3 for exit")

            reverse_input = int(input("Enter a number : "))

            if reverse_input == 1 :
                print(my_list)
                print(my_list[::-1])

            elif reverse_input == 2 :
                rev_start_input = int(input("Enter Starting index value : "))
                rev_end_input = int(input("Enter ending index value : "))
                a = my_list[rev_start_input:rev_end_input]
                print("Modified list : ",a)
                print("Reverse list",a[::-1])
                
            else:
                print(listelement)
                listelement()


        elif i == 7 :
            print("welcome to clear session !!!!")
            print(my_list)
            my_list.clear()
            print("After clear : ",my_list)
            listelement()

        elif i == 8 :
            print("Thank you for using a Program !!!!")
            print("Have a nice day !!!!")
            print("BYE-BYE")
            listelement()

listelement()