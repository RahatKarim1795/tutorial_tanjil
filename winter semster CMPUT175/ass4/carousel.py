import json
import os
import time
# from art import current_frame,current_only_frame,going_left,going_right,add_only_frame,adding_left,adding_only_left,adding_only_right,adding_right,del_frame,del_only_frame
from art import *

class Frame:
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self

        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class Carousel:
    def __init__(self):
        self.current = None
        self.current_size = 0
        self.max_size = 5


    def add(self, item, direction, emojis):

        # print(emojis[0]['emojis']['grape'])

        for i in range(len(emojis)):
            for title,dict in emojis[i].items():
                if title == 'emojis':
                    for name,pic in dict.items():
                        if name == item:
                            new_node = Frame(pic,None,None)
                            


        current = self.current

        if direction == None:
            self.current = new_node

        elif self.current_size==1:
            new_node.setNext(current)
            new_node.setPrevious(current)
            current.setPrevious(new_node)
            current.setNext(new_node)

            self.current = new_node

        else:
            if direction == "left":
                new_node.setNext(current)
                new_node.setPrevious(current.getPrevious())
                current.getPrevious().setNext(new_node)
                current.setPrevious(new_node)

            elif direction == "right":
                new_node.setNext(current.getNext())
                new_node.setPrevious(current)
                current.getNext().setPrevious(new_node)
                current.setNext(new_node)
            
            self.current = new_node

        self.current_size+=1



    def remove(self):

        current = self.current

        if self.current_size == 1:
            self.current = None

        else:
            before = current.getPrevious()
            after = current.getNext()
            before.setNext(after)
            after.setPrevious(before)

            self.current = before

        self.current_size-=1
    
    def go_left(self):
        current = self.current
        self.current = current.getPrevious()
    
    def go_right(self):
        current = self.current
        self.current = current.getNext()

    def getSize(self):
        return self.current_size


    def __str__(self):

        current = self.current

        if self.current_size==1:
            string = current_only_frame(current.getData())

        elif self.current_size>1:
            left = current.getPrevious()
            right = current.getNext()
            string = current_frame(current.getData(),left.getData(),right.getData())

        return string
    

def load_emojis(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        emojis = json.load(file)

    return emojis

def clear_terminal():
    print("\033[2J\033[H", end='')

def clear_line():
    print("\033[K", end='')

def move_cursor(x, y):
    print(f"\033[{x};{y}H", end='')
    
def main():

    emojis = load_emojis('emojis.json')

    command = ""
    carousel = Carousel()

    clear_terminal()


    while command.upper()!="Q":
        clear_terminal()

        if carousel.getSize() == 0:
            move_cursor(1,0)
            print("Type any of the following commands to perform the action:")
            move_cursor(2,9)
            print("ADD: Add an emoji frame")
            move_cursor(3,9)
            print("Q: Quit the program")
            move_cursor(4,0)
            command = input(">> ").upper()

        elif carousel.getSize() == 1:
            move_cursor(1,0)
            print(carousel)
            move_cursor(12,0)
            print("Type any of the following commands to perform the action:")
            move_cursor(13,9)
            print("ADD: Add an emoji frame")
            move_cursor(14,9)
            print("DEL: Delete current emoji frame")
            move_cursor(15,9)
            print("INFO: Get information about the current emoji frame")
            move_cursor(16,9)
            print("Q: Quit the program")
            move_cursor(17,0)
            command = input(">> ").upper()

        else:
            move_cursor(1,0)
            print(carousel)
            move_cursor(12,0)
            print("Type any of the following commands to perform the action:")
            move_cursor(13,9)
            print("L: Move Left")
            move_cursor(14,9)
            print("R: Move Right")
            move_cursor(15,9)
            print("ADD: Add an emoji frame")
            move_cursor(16,9)
            print("DEL: Delete current emoji frame")
            move_cursor(17,9)
            print("INFO: Get information about the current emoji frame")
            move_cursor(18,9)
            print("Q: Quit the program")
            move_cursor(19,0)
            command = input(">> ").upper()


        if command == "ADD":
            if carousel.getSize()==carousel.max_size:
                move_cursor(19,0)
                print("The carousel is full. You cannot add any more emoji frames.")
            elif carousel.getSize()==0:
                move_cursor(5,0)
                print("What do you want to add?")
                move_cursor(6,0)
                item = input(">> ").lower()
                clear_terminal()
                move_cursor(1,0)
                print(add_only_frame())
                time.sleep(0.5)
                direction = None
                carousel.add(item, direction, emojis)

            elif carousel.getSize()==1:
                move_cursor(17,0)
                print("What do you want to add?")
                move_cursor(18,0)
                item = input(">> ").lower()
                move_cursor(19,0)
                print("On which side do you want to print the emoji frame?(left/right)")
                move_cursor(20,0)
                direction = input(">> ").lower()
                clear_terminal()
                move_cursor(1,0)
                if direction == "left":
                    print(adding_only_left())
                else:
                    print(adding_only_right())
                time.sleep(0.5)
                carousel.add(item, direction, emojis)

            else:
                move_cursor(19,0)
                print("What do you want to add?")
                move_cursor(20,0)
                item = input(">> ").lower()
                move_cursor(21,0)
                print("On which side do you want to print the emoji frame?(left/right)")
                move_cursor(22,0)
                direction = input(">> ").lower()
                clear_terminal()
                move_cursor(1,0)
                l_emoji = carousel.current.getPrevious().getData()
                r_emoji = carousel.current.getNext().getData()
                if direction == "left":
                    print(adding_left(l_emoji,r_emoji))
                else:
                    print(adding_right(l_emoji,r_emoji))
                time.sleep(0.5)
                carousel.add(item, direction, emojis)
                
            
        elif command == "DEL":
            clear_terminal()
            move_cursor(1,0)
            if carousel.getSize()==1:
                print(del_only_frame())
            else:
                l_emoji = carousel.current.getPrevious().getData()
                r_emoji = carousel.current.getNext().getData()
                print(del_frame(l_emoji,r_emoji))
            time.sleep(0.5)
            carousel.remove()

        elif command == "INFO":
            # TODO
            pass

        elif command == "L":
            clear_terminal()
            move_cursor(1,0)
            l_emoji = carousel.current.getPrevious().getData()
            r_emoji = carousel.current.getNext().getData()
            print(going_left(l_emoji,r_emoji))
            time.sleep(0.5)
            carousel.go_left()

        elif command == "R":
            clear_terminal()
            move_cursor(1,0)
            l_emoji = carousel.current.getPrevious().getData()
            r_emoji = carousel.current.getNext().getData()
            print(going_right(l_emoji,r_emoji))
            time.sleep(0.5)
            carousel.go_right()

        elif command == "Q":
            clear_terminal()
            print("Thank you for using the program. Goodbye!")

        

main()
# emojis = load_emojis('emojis.json')
# # print(emojis)
# # for i in range(len(emojis)):
# #     for key,value in emojis[i].items():
# #         if key == "grape":
# #             print(value)

# a = emojis[0]

# print(emojis[0]['emojis']['grape'])

# print(going_right('🍇','🍉'))
