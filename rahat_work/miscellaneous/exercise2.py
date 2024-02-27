condition = True

while condition == True:
    fish = input("Enter fish: ")

    if fish == "trout":
        print("accept")
    elif fish == "finish":
        print("bye bye")
        break
    else:
        print("back to the sea")
