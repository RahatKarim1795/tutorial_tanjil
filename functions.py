# # define function
#     # explain what the function does

# # call function
#     # call the function where the work needs to be done



# # function 1
# def print_function():
#     print("Print Function")

# print_function()


# # function 2
# def add_function():
#     x = input("Enter number 1: ")
#     y = input("Enter number 2: ")
#     z = int(x) + int(y)
#     return(z)

# x = add_function()
# print(x)

# # function 3
# def name():
#     x = input("Enter name: ")
#     return(x)

# n = ""
# while n != "finish":
#     n = name()
#     print(n)

# for i in range(3):
#     name()




# function 4
# def a(x):
#     print(x)

# x = input("Type what you want: ")
# a(x)



# # function 5 
# def argument_function(x):
#     print("you typed: " + x)

# for i in range(3):
#     y = input("Type what you want: ")
#     argument_function(y)



# # function 6
# def argument_function(x):
#     if x == "finish":
#         print("bye bye")
#     else:
#         print("you typed: " + x)

# y = ""
# while y!= "finish":
#     y = input("Type what you want: ")
#     argument_function(y)


# function 7
# def calc_difference(x, y):
#     z = x - y
#     if z < 0:
#         z *= -1
#     return(z)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# c = calc_difference(a,b)
# print("Difference is: " + str(c))
    
    
# function 8
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)



# function 9
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5)
# print("Factorial of 5 is: ", result)

# x = input("Enter number: ")
# result = factorial(int(x))
# print("Factorial of " + x + " is: ", result)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(4)



# function 10

# def comparison():
#     a = int(input("enter 1: "))
#     b = int(input("enter 2: "))
#     if a>=b:
#         return(a)
#     else:
#         return(b)
    
# print("enter two values to find which is bigger!!")
# number = comparison()
# print("bigger number is: " + str(number))

# x = number * 2

# def comparison():
#     a = int(input("enter 1: "))
#     b = int(input("enter 2: "))
#     if a>=b:
#         print("bigger number is: " + str(a))
#     else:
#         print("bigger number is: " + str(b))
    
# print("enter two values to find which is bigger!!")
# comparison()
