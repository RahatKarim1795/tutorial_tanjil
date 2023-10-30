## practice 3
# write a function that checks if the number entered is prime or not
# a prime number is only divisible by 1 and itself nothing in between
## practice 3

def check_prime():
    user_input = int(input("Enter the number you want to check: "))
    for i in range(2, user_input):
        if user_input % 2 == 0:
            print("Not prime")
            break
        else:
            print("Prime")
            break

check_prime()




