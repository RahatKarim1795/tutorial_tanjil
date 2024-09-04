import os

ANSI = {
"RED": "\033[31m",
"GREEN": "\033[32m",
"BLUE": "\033[34m",
"HRED": "\033[41m",
"HGREEN": "\033[42m",
"HBLUE": "\033[44m",
"UNDERLINE": "\033[4m",
"RESET": "\033[0m",
"CLEARLINE": "\033[0K",
"MAGENTA": "\033[105m",
"YELLOW": "\033[103m",
"ORANGE": "\033[48;2;255;165;0m"
}


def move_cursor(x, y):
    print(f"\033[{x};{y}H", end='')

os.system("") # Enables ANSI escape codes in terminal
# Clears the terminal. What happens if this gets removed?
if os.name == "nt": # for Windows
    os.system("cls")
else: # for Mac/Linux
    os.system("clear")


print(ANSI["UNDERLINE"] + ANSI["BLUE"] + "VT100 SIMULATOR" + ANSI["RESET"])


move_cursor(3,0)
print("Enter a text colour: ")

move_cursor(4,0)
print("Enter a background colour: ")

text = 0
back = 0

while text != "EXIT" or back!= "EXIT":
    move_cursor(3,21)
    text = input("").upper().strip()
    move_cursor(4,28)
    back = input("").upper().strip()

    if (text not in ANSI) or (back not in ANSI):
        move_cursor(3,21)
    
    print(ANSI["CLEARLINE"])


    print(ANSI[back] + ANSI[text] + "VT100 SIMULATOR" + ANSI["RESET"])





