class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

        
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack.")
        else:
            return self.items.pop()


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
    a=1
