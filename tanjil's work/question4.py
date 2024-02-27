def sign_up():
    user_sign_in = input("Do you want to 'sign in' or 'sign up'?: ")
    if user_sign_in == 'sign in':
        user_name = input("Enter username: ")
        user_pass = input("Enter password: ")
        filename1 = 'user_name.txt'
        filename2 = 'password.txt'
        with open(filename1) as file1, open(filename2) as file2:
            line1 = file1.readlines()
            line2 = file2.readlines()

            if line1 == user_name and line2 == user_pass:
                print(f'Welcome {user_name} to you account.')
            else:
                print("Sorry the username or password is incorrect please try signing up.")



    else:
        filename1 = 'user_name.txt'
        filename2 = 'password.txt'

        with open(filename1, 'a') as file1, open(filename2, 'a') as file2:

            user_name1 = input("Enter username: ")
            user_pass2 = input("Enter password: ")

            file1.write(f'{user_name1}\n')
            file2.write(f'{user_pass2}\n')

            print("You have successfully signed up!")


# sign_up()

grid = [[1,2,3],[2,3,4]]
row = 0
col = 0
for i in grid:
    row+=1
    col = 0
    for j in i:
        col+=1

print(row,col)