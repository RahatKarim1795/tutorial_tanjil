#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
        
    # The instructions specify not to handle the exception within the Stack class.
    # This means you should not use a try...except block within these methods to catch
    # the Exception you're raising. Instead, any code that uses this class and calls
    # pop() or peek() on an empty stack should be responsible for handling the potential exception.
        
    def pop(self):

        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack.")
        else:
            return self.items.pop()

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK

    def peek(self):

        if self.isEmpty():
            raise Exception("Cannot peep from an empty stack.")
        else:
            return self.items[len(self.items)-1] 

    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        if not self.isEmpty():
            self.items = []
        else:
            pass  


def main():
    stack_object = Stack()

    # stack_object.push(1)
    # stack_object.push(2)

    # stack_object.pop()
    try:
        stack_object.pop()
    except Exception as actionException:
        print(actionException.args[0])

    # print(stack_object.peek())
    # stack_object.clear()

    stack_object.show()

main()