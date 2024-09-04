from queues import BoundedQueue
from stack import Stack
import os

ANSI = {
"AA": "\033[41m", #red
"BB": "\033[44m", #blue
"CC": "\033[42m", #green
"DD": "\033[48;2;255;165;0m", #orange
"EE": "\033[103m", #yellow
"FF": "\033[105m", #magenta
"RESET": "\033[0m",
"  ": "",
"--" : ""
}

def clear_line():
    print("\033[K", end='')

def move_cursor(x, y):
    print(f"\033[{x};{y}H", end='')

def check_finsh(flask_stacks, completed):
    # Create a set of current completed flasks based on the new criteria
    current_completed = set()

    for name, stack in flask_stacks.items():
        item_counts = {}
        total_items = len(stack.items)

        # Count the occurrence of each item
        for item in stack.items:
            item_counts[item] = item_counts.get(item, 0) + 1

        # Check if any item counts to 3 and total items are 3, add to current completed
        if any(count == 3 for count in item_counts.values()) and total_items == 3:
            current_completed.add(name)

    # Update the completed list based on current_completed set
    # Add newly completed flasks
    for name in current_completed:
        if name not in completed:
            completed.append(name)

    # Remove flasks that are no longer completed
    for name in completed[:]:  # Iterate over a copy of the list to safely modify the original list
        if name not in current_completed:
            completed.remove(name)

    return completed


# def check_finsh(flask_stacks,completed):

#     for name,stack in flask_stacks.items():
#         item_counts = {}
#         max = len(stack.items)

#         # if max == 3:
#         for item in stack.items:
#             if item in item_counts:
#                 item_counts[item] += 1
#             else:
#                 item_counts[item] = 1

#         for item, count in item_counts.items():
#             if count == 3 and max==3:
#                 if name not in completed:
#                     completed.append(name)
#             else:
#                 if name in completed:
#                     index = 0
#                     for item in completed:
#                         if item == name:
#                             completed.pop(index)
#                             index+=1
            
#     return completed


     
def show_flasks(flask_stacks,completed):

    no_of_flasks = len(flask_stacks)

    flask_list = [["  " for _ in range(no_of_flasks)] for _ in range(4)]
    
    row = 0
    for flask_name, value in flask_stacks.items():
        col = no_of_flasks-1 # change the order of stack.items to behave like a stack visually
        for item in value.items:
            flask_list[col][row] = item
            col-=1
        row += 1

    for col in range(no_of_flasks):

        empty_spaces=0
        temp = []  # Initialize an empty list to hold non-empty elements

        for row in range(4):  # Loop through each row in the column
            if flask_list[row][col] != "  ":  # Check if the element is not an empty space
                temp.append(flask_list[row][col])  # Add the non-empty element to the temp list
            else:
                empty_spaces+=1

        # Reconstruct the column with empty spaces at the top
        for row in range(empty_spaces):
            flask_list[row][col] = "  "

        # Fill the rest of the column with the non-empty elements
        temp_list_position = 0
        for row in range(empty_spaces, 4):
            flask_list[row][col] = temp[temp_list_position]
            temp_list_position+=1

        
    completed = check_finsh(flask_stacks,completed)

    for row in flask_list:
        for item in row:
            if completed:
                for flask_no in completed:
                    c = flask_no - 1
                    flask_list[0][c] = "--"
            
            if item == "--":
                print("+--+ ",end="")
            else:
                print(f'|{ANSI[item]}{item}{ANSI["RESET"]}| ',end="")


        print()

    for i in range(no_of_flasks):
        print(f'+--+ ', end="")
    print()
    for i in range(no_of_flasks):
        print(f'  {i+1}  ', end="")


def lab_work(file):
    chemicalTray = BoundedQueue(4)

    with open(file, 'r') as f:
        instruction = f.readline().strip()

        no_of_flask = int(instruction.split(" ")[0])
        no_of_chemicals = int(instruction.split(" ")[1])

        flask_stacks = {}

        for i in range(no_of_flask):
            flask_stacks[int(i+1)] = Stack()

        running = True

        #start reading from 2nd line
        while running == True:
            line = f.readline().strip()
            if not line:
                running = False
            else:
                if len(line) == 2:
                    if not chemicalTray.isFull():
                        chemicalTray.enqueue(line)
                    
                else:
                    flask_no = int(line[2])
                    chemicals_to_dq = int(line[0])

                    for i in range(chemicals_to_dq):
                        chemical_name = chemicalTray.dequeue()

                        if flask_stacks[flask_no].size() < 4:
                            flask_stacks[flask_no].push(chemical_name)
    
    return flask_stacks

def change_flask(source,destination,flask_stacks):

    for name,stack in flask_stacks.items():
        if name == int(source):
            chem = stack.pop()

    for name,stack in flask_stacks.items():
        if name == int(destination):
            if chem:
                stack.push(chem)
        

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_loop(flask_stacks):
    no_of_flasks = int(len(flask_stacks))

    in1 = ""
    in2 = ""
    clear_screen()
    completed = []

    while in1 != "exit" or in2 != "exit":
        move_cursor(0,0)
        print("Magical Flask Game")
        move_cursor(3,0)
        clear_line()
        print("Select Source Flask: ")
        move_cursor(4,0)
        clear_line()
        print("Select Destination Flask: ")
        move_cursor(6,0)
        show_flasks(flask_stacks,completed)
        move_cursor(3,22)
        in1 = input("")
        move_cursor(4,27)
        in2 = input("")
        # if not in1.isdigit() or not in2.isdigit() or in1>int(no_of_flasks) or in1<1 or in2>int(no_of_flasks) or in2<1:
        #     move_cursor(5,0)
        #     print("Wrong input")
        # else:
        change_flask(in1,in2,flask_stacks)



def main():
    flask_stacks = lab_work("chemicals.txt")
    # print(flask_stacks)
    # for n,s in flask_stacks.items():
    #     print(s)
    game_loop(flask_stacks)
    clear_screen()
    # show_flasks(flask_stacks)

    # for n,s in flask_stacks.items():
    #     print(s)



main()

# a = [[1,1,1],[1,1,1],[1,1,1]]
# r=0
# c=0

# for i in range(len(a)):
#     for j in range(i):
#         print(a[r][c], end="")
#         c+=1
#     print()
#     r+=1


