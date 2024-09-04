from queues import BoundedQueue
from stack import Stack

def lab_work(file):
    chemicalTray = BoundedQueue(4)

    with open(file, 'r') as f:
        instruction = f.readline().strip()

        no_of_flask = int(instruction.split(" ")[0])
        no_of_chemicals = int(instruction.split(" ")[1])

        flask_stacks = {}

        for i in range(no_of_flask):
            flask_name = "flask" + str(i+1)
            flask_stacks[flask_name] = Stack()

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
                        flask_name = "flask" + str(flask_no)
                        if flask_stacks[flask_name].size() < 5:
                            flask_stacks[flask_name].push(chemical_name)

        # for flask_name,stack in flask_stacks.items():
        #     print(flask_name + " = ", end="")
        #     stack.show()
    
    return flask_stacks
 
def show_flasks(flask_stacks):

    no_of_flasks = len(flask_stacks)

    # flask_list = [["  " for _ in range(5)] for _ in range(no_of_flasks)]
    flask_list = [["  " for _ in range(no_of_flasks)] for _ in range(4)]
    row = 0
    
    col = 0
    for flask_name, value in flask_stacks.items():
        row = 0
        for item in value.items:
            flask_list[row][col] = item
            row+=1
            
        col += 1

    # print(flask_list)



    # for flask in flask_list:

    #     if flask[3] == "  ":
    #         # print("YES")
    #         while(flask[3] != "  "):
    #             flask[3] = flask[2]
    #             flask[2] = flask[1]
    #             flask[1] = flask[0]
    #             flask[0] = "  "


    for row in flask_list:
        for item in row:
            print(f'|{item}| ', end="")
        print()

    for i in range(no_of_flasks):
        print(f'+--+ ', end="")
    print()
    for i in range(no_of_flasks):
        print(f'  {i+1}  ', end="")

def main():
    flask_stacks = lab_work("chemicals.txt")
    show_flasks(flask_stacks)

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


