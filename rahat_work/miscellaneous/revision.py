## question 1
## file i/o writing
# Create a file users.txt
# Ask user for a username and save it in this file


def user():
    username = input("Enter username: ")
    f = open("users.txt", "a")
    f.write(username + '\n')
    f.close()

# user()


## question 2
## file i/o writing
# Create a file users.txt
# Ask user how many names he wants to save
# Take that many inputs and save it in the file
# along with an increasing number
# (e.g.: input: rahat
#        in file: 2 rahat
#        input: rht
#        in file: 3 rht)


def user1():
    inputs = input("How many inputs: ")

    with open('users.txt') as f:
        for line in f:
            continue
        last_line = line
    
    # last_number = int(last_line.split(' ', 1)[0])

    split_string = last_line.split(' ', 1) # split string at space; split it only once
    # split string = ['6', 'john cena']
    last_number = split_string[0] # take the first element from the split string

    print(last_number)


    for i in range(int(inputs)):
        last_number+=1
        username = input("Enter username: ")
        f = open("users.txt", "a")
        f.write(str(last_number) + " " + username + '\n')
    f.close()

# user1()



## question 3
## file i/o reading
# Use the previous file users.txt
# Ask user the name he wants to search
# If found the program tells the user name
# has been found along with the number of entry
# (e.g.: input: rht
#        output: Name found at entry 3)


def user2():
    search = input("Search for username: ")

    found = False

    f = open('users.txt', 'r')
    each_line = f.readline()

    while each_line:
        
        split = each_line.split(' ', 1)

        if split[1].strip() == search:
            print(f'Name found at entry: {split[0]}')
            found = True
            break

        each_line = f.readline()

    f.close()

    if found == False:
        print("Name not found!")

    # with open('users.txt') as f:
    #     for line in f:

    #         split_string = line.split(' ', 1)

    #         if split_string[1].strip() == search:
    #             print("Name found at entry: " + split_string[0])
    #             break



            # entry, username = line.split(' ', 1)
            # if username.strip() == search:
            #     print("Name found at entry: " + entry)
            #     break
        # else:
        #     print("Name not found!") # only executes if the loop does not encounter a break statement


    # f1 = open("users.txt", "r")
    # f2 = open("users.txt", "r")
    # f3 = open("users.txt", "r")

    # print(f1.read())

    # print(f2.readlines())

    # print(f3.readline())
    # print(f3.readline())
    

# user2()



## question 4
# file i/o read & write
# First create a file called user_name.txt and password.txt
# Create a function that asks the user if he 
# wants to sign in or sign up (create an account)
# When the user wants to sign up ask for the user name first and 
# save it in the user_name.txt along with a number (e.g: 1 rahat)
# Then ask for the password and save it in password.txt with the same number
# (e.g: 1 rahat1234)
# So the number in front of the user name and password
# will be matched for checking
# When user wants to sign in, he is asked for username first,
# then password. If they both match the same entry in the files
# display a welcome msg


matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    a_row = ''
    for col in row:
        a_row += str(col) + " "
    print(a_row)

print()

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()

a_row = "1 2 3 " # print then delete
a_row = "4 5 6 " # print then delete

a_row = ""
a_row = "7"
a_row = "78"
a_row = "789"


file_name = "data_0.txt"

f = open(file_name, "r")

with open(file_name) as file1:
    for line in file1:
        print(line)