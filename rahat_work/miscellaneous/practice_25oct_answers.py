# For each of the questions utilize a main() function and an individual function for each
# other functions must always be called in main() example is given in first question






## practice 1
# Write a function that accepts a string 
# and counts the number of upper and lower case letters

# def count_letters(input):
#     count = 0
#     upper = 0
#     lower = 0
#     for i in input:
#         count+=1
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#     print("Total letters: " + str(count) + "\nUppercase: " + str(upper) + "\nLowercase: " + str(lower))

# def main():
#     a =  input("Enter string to count upper and lower case: ")
#     count_letters(a)

# main()

## practice 1








## practice 2
# Write a function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., "madam" or "nurses run"

# def check_palindrome(input):

#     input = input.replace(" " , "")

#     forward = []
#     backward = []
#     length = len(input)
#     position = len(input)-1
#     pali = True

#     for i in input:
#         forward.append(i)
    
#     for i in range(length):
#         letter = forward[position]
#         position-=1
#         backward.append(letter)

#     for i in range(length-1):
#         if forward[i] == backward[i]:
#             continue
#         else:
#             pali = False
#             break

#     if pali == True:
#         print("That's a palindrome!")
#     else:
#         print("That aint it!")



# def main():
#     a = input("Enter word or phrase to check palindrome: ")
#     check_palindrome(a)

# main()

## practice 2




## practice 3
# write a function that checks if the number entered is prime or not
# a prime number is only divisible by 1 and itself nothing in between

# def check_prime(input):
#     prime = False
#     start = 2

#     if input == 1:
#         print("Not prime")
#     elif input == 2:
#         print("The number is prime")
#     else:
#         for i in range(2, input):
#             if input % i == 0:
#                 print("Not prime")
#                 break
#             else:
#                 prime = True

#     if prime == True:
#         print("The number is prime")

    

# def main():
#     a = int(input("Enter number: "))
#     check_prime(a)

# main()


## practice 3



## practice 4
# write a function that asks user to enter a floating point number
# the function then counts total number of digits and lets the user know
# it also stores all the digits in a list and shows them to the user

# def count_digits(input):
#     digit_count = len(input) - 1
#     digits = []

#     print("There are " + str(digit_count) + " digits: ")

#     for i in input:
#         if i != ".":
#             digits.append(i)
#             print(i)
#         else:
#             continue


# def main():
#     a = input("Enter number: ")
#     count_digits(a)

# main()

## practice 4


## practice 5
# write a function that first asks if the user is ready
# if ready, User is asked to type in "5940"
# the function tells the user how fast they typed the number
# use the following function and "import time"

# import time

# def get_typing_time () -> (float):

#     start = time.time()
#     input("Type the following '5940': ")
#     user_time = round(time.time() - start, 2)
#     print(f"Result: {user_time} seconds")

#     return user_time

# def main():
#     a = input("Are you ready? (y/n): ")
#     if a.lower()=='y':
#         get_typing_time()


# main()

## practice 5


## practice 6
# this program tests the user's math knowledge 
# and gives points according to the answers
# write a function that asks the user to type a prime number
# if the number is a prime number give 5 points, let the user know and go to next round
# then the user is asked to write the value of pi until 4 digit after decimal point (3.1415)
# if the full number is correct give 5 points. 1 point is deducted for each digit mistake (e.g. user input=3.1425; points=4)
# go to next round
# now user is asked to give the answer to:495x12
# if user answers correctly within 3 seconds give 5 points
# if within 3-6 seconds 3 points; if any later than 6 seconds 1 point
# incorrect answer gets -3 points
# finally let the user know their total points

# def check_prime(input):

#     prime = False

#     if input == 1:
#         print("Not prime")
#     elif input == 2:
#         print("The number is prime")
#     else:
#         for i in range(2, input):
#             if input % i == 0:
#                 print("Not prime")
#                 return False
#             else:
#                 prime = True

#     if prime == True:
#         print("The number is prime")
#         return True

# def round_one_prime():

#     i = int(input("Enter a prime number: "))
#     result = check_prime(i)
#     if result == True:
#         return 5
#     else:
#         return 0

# def round_two_pi():

#     user_input = input("Enter value of pi up to 4 digits after decimal: ")

#     point = 5

#     digits = []

#     for i in user_input:
#         if i != ".":
#             digits.append(i)
#         else:
#             continue
    
#     a = 0

#     pi = ['3','1','4','1','5']

#     for i in range(5):
#         if digits[a] != pi[a]:
#             point += -1
#         a+=1
    
#     return point

# import time

# def get_typing_time () -> (float):

#     start = time.time()
#     answer = input("Answer 495x12: ")
#     user_time = round(time.time() - start, 2)
#     print(f"Result: {user_time} seconds")

#     return user_time,answer

# def round_three_multi():
#     speed,answer = get_typing_time()
#     if speed < 3:
#         point = 5
#     elif speed < 6 and speed > 3:
#         point = 3
#     elif speed > 6:
#         point = 1
#     elif answer != "5940":
#         point = -1

#     return point



# def main():

#     total_points = 0
#     point3 = 0
#     point2 = 0
#     point1 = 0

#     for i in range(40):
#         print("#", end="")
#     print("\nTest your math knowledge!")
#     for i in range(40):
#         print("#", end="")
#     print("\n")
#     a = input("Ready for round 1? (y/n): ")
#     if a.lower() == 'y':
#         point1 = round_one_prime()
#     elif a.lower() == 'n':
#         quit()
#     total_points+=point1


#     a = input("Ready for round 2? (y/n): ")
#     if a.lower() == 'y':
#         point2 = round_two_pi()
#     elif a.lower() == 'n':
#         b = input("Show total points? (y/n): ")
#         if b.lower() == 'y':
#             print("Total Points: " + str(total_points))
#             quit()
#         else:
#             quit()
    
#     total_points += point2

#     a = input("Ready for round 3? (y/n): ")
#     if a.lower() == 'y':
#         point3 = round_three_multi()
#     elif a.lower() == 'n':
#         b = input("Show total points? (y/n): ")
#         if b.lower() == 'y':
#             print("Total Points: " + str(total_points))
#             quit()
#         else:
#             quit()
    
#     total_points+=point3

#     print("Total Points: " + str(total_points))

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() == 'y':
#         main()
#     else:
#         quit()


# main()