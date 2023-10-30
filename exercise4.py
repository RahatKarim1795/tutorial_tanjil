# create a loop that will keep taking the temperature of a nuclear reactor
# if the temp is normal (500 - 950) degree celcius system will run normally
# if the temp exceeds 950 system is shut down and an error msg is shown to user
# if temp is lower than 500 just let user know

x = True

while x == True:
    current_temp = int(input("Enter temperature: "))

    if(current_temp<500):
        print("current temperature too low. check reactor")

    elif(current_temp>950):
        print("TEMPERATURE OVERLOAD! DANGER")
        x = False

    else:
        continue