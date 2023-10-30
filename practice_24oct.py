# ## practice 1
# def define_number():
#     while True:
#         user_input = input("Enter your number: ")

#         if user_input.isdigit():
#             if int(user_input) % 2 == 0:
#                 print("The number is even.")
#             elif int(user_input) % 2 == 1:
#                 print("The number is odd.")

#         elif user_input == "finish":
#             break
#         else:
#             print("Invalid Input")





# def main():
#     print("Enter a number to see if it's odd or even and type finish to end.")
#     define_number()

# main()
## practice 1



## practice 2

# user will type in names of students to store in a file student.txt
# if user wants to see all student names show all names
# user can also search for a student name. function will say student exists or not

def new_student():
    f = open("student.txt", "a", encoding = "utf-8")

    new_name = input("Enter name of student: ")

    f.write("\n" + new_name)

    f.close()

def search_student():
    name = input("Enter name to search: ")
    f = open("student.txt", "r", encoding = "utf-8")

    all_students = f.readlines()
    found = False
    for line in all_students:
        if line == name + '\n':
            print("Student exists")
            found = True
        else:
            continue
            
    if found == False:
        print("Student not found!")

def main1():
    x = input("Press 'N' to input new student and 'S' to search: ")
    if x == "N" or x == "n":
        new_student()
    elif x == "S" or x== "s":
        search_student()

main1()

## practice 2
