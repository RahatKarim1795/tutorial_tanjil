# Exercise 3
# ceate a for loop to take name ipnut from x users.
# the x will also be defined by the user.
# the program will then show the user the given input



n2 = int(input("Enter number of users: "))

# for i in range(n2):
#     n1 = input("Enter name: ")
#     print(n1)
a = n2

for x in range(n2):
    n1 = input("Enter name: ")
    print(n1)
    a -= 1
    print(a + "inputs left")


# [0,1,2...n2]