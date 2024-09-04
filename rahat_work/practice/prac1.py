# Make a program that asks the user if he is student, teacher or admin

# If teacher the user can select a course id from a given list and
# give marks to a student, which will be saved in the marks text file
# inputs student id, mark and grade

# If student, they can enter their id and course id to see their mark and grade
# if it is not availabe let them know

# Admin can add courses and students to the database

# make a class called Students with attributes:
# student_id, student_name, cgpa

# make a class called courses with attributes:
# course_id, course_name, lecturer

# make a class called marks with attributes:
# course_id, student_id, mark, grade

# Make relevant functions in each class (constructor and string function necessary)
# If needed make functions outside the classes

class Students:

    def __init__(self, id, name, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    
    def __str__(self) -> str:
        return f"ID: {self.id}, Name: {self.name}, CGPA:{self.cgpa}"
    
    def see_marks(self, course):
        id = self.id

        with open("marks.txt", "r", encoding="utf-8") as file:
            # Read all lines from the file
            line_info = [line.strip().split('|') for line in file]

            if line_info[1] == id:
                print(f'{line_info[0]}: {line_info[2]}, {line_info[3]}')

    # def add_student(self, )

def see_marks(s_id, c_id):

    with open("marks.txt", "r", encoding="utf-8") as file:
            # Read all lines from the file
            line_info = [line.strip().split('|') for line in file]

            if line_info[1] == s_id and line_info[0] == c_id:
                print(f'{line_info[0]}: {line_info[2]}, {line_info[3]}')

class Courses:
    
    def __init__(self, id, name, lecturer):
        self.name = name
        self.id = id
        self.lecturer = lecturer

    
    def __str__(self) -> str:
        return f"Course ID: {self.id}, Name: {self.name}, Lecturer:{self.lecturer}"
    
class Marks:
    def __init__(self, c_id, s_id, mark, grade):
        self.c_id = c_id
        self.s_id = s_id
        self.mark = mark
        self.grade = grade

    
    def __str__(self) -> str:
        return f"Course ID: {self.c_id}, Student ID: {self.s_id}, Mark:{self.mark}, Grade:{self.grade}"
    
def main():
    x = input("Are you student(s), lecturer(l) or admin(a)?")

    if x.lower()=="s":
        print("To see marks:\n")
        st_id = input("Input your id: ")
        co_id = input("Input course id: ")
        see_marks(st_id,co_id)

floa = 1.2
int(floa)