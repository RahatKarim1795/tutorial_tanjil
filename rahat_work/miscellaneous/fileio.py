# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists/ This mode is typically used when you want to ensure that a new file is created and you don't want to overwrite an existing file.
 

# function 1
# x = "whatsgood.txt"
# f = open(x)

# print(f.read())


# function 2

# f = open("whatsgood.txt", "r" , encoding = "utf-8")
# print(f.read())

# function 3
# f = open("whatsgood.txt", "r")
# print(f.read(2))

# function 4

# f = open("whatsgood.txt", "r", encoding = "utf-8")
# print(f.readline())
# print(f.readline())

# function 5 append/edit

# t = "whatsgood.txt"
# f = open(t, "a", encoding = "utf-8")
# f.write("\nExtra Stuff")
# f.close()

# x = "whatsgood.txt"
# f = open(x, "r", encoding = "utf-8")
# print(f.read())


# # function 6 write/overwrite

# f = open("whatsbetter.txt", "w", encoding = "utf-8")
# f.write("New content!!")
# f.close()
# f = open("whatsbetter.txt", "r", encoding = "utf-8")
# print(f.read())

# # function 7 create

# f = open("myfile.txt", "x", encoding = "utf-8")
# f = open("myfile.txt", "w", encoding = "utf-8")

# function 8 delete

# import os
# os.remove("tobedeleted2.txt")
# if os.path.exists("tobedeleted.txt"):
#   os.remove("tobedeleted.txt")
# else:
#   print("The file does not exist")
# os.rmdir("deleteex")


file_name = "data_0.txt"

f = open(file_name, "r")

with open(file_name) as file1:
    for line in file1:
        print(line)