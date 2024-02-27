# user will type in names of students to store in a file student.txt
# if user wants to see all student names show all names
# user can also search for a student name. function will say student exists or not\

def write_names(filename: str) -> list[str]:
    user_input = input("Enter your name: ")
    student_file = open(filename, "a", encoding="utf-8")

    student_file.write(user_input + "\n")
    student_file.close()

def show_names(filename: str) -> list[str]:
    show_input = input("Do you want to see the names of the students? Type 'Y' or 'N' \n")

    if show_input.upper() == 'Y':
        print("The names of the students are: ")

        with open(filename, 'r', encoding="utf-8") as student_file:
            for name in student_file:
                print(name.strip())
        
        # f = open(filename, "r")

        # print(f.readlines())

    elif show_input.upper() == 'N':
        print("")
    else:
        print("Invalid input!")



def search_name(filename: str) -> list[str]:

    search_input = input("Enter the name you are looking for: ")

    student_file = open("student.txt", "r", encoding="utf-8")

    name1 = student_file.readlines()

    if search_input + '\n' in name1:
        print("The name " + str(search_input) + " does exist!")
    else:
        print("The name " + str(search_input) + " does not exist!")


def main(filename: str) -> list[str]:
    write_names(filename)
    show_names(filename)
    search_name(filename)

main("student.txt")