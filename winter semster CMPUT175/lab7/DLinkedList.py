class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
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


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def add(self, item):
        # adds the item to the start of the list
        # TODO

        new_node = DLinkedListNode(item,None,None)

        if self.__head:
            new_node.setNext(self.__head)
            self.__head.setPrevious(new_node)
            self.__head = new_node

        else:
            self.__head = new_node
            self.__tail = new_node

        self.__size +=1 



    def remove(self, item):
        # removes the first element in the list that is equal to the item
        # TODO
        current = self.__head

        while current:
            if current.getData() == item:
                
                if current == self.__head:
                    self.__head = current.getNext()
                    if self.__head:
                        self.__head.setPrevious(None)
                    else:
                        self.__tail = None
                    return True
                
                elif current == self.__tail:
                    current.getPrevious().setNext(None)
                    self.__tail = current.getPrevious()
                    return True
                
                else:
                    before = current.getPrevious()
                    after = current.getNext()
                    before.setNext(after)
                    after.setPrevious(before)
                    return True   

            current = current.getNext()

        return False



    def append(self, item):
        # adds a new node to the tail of the list with item as its data
        # TODO

        new_node = DLinkedListNode(item, None, None)

        # tail = self.__tail

        if self.__size == 0:
            self.add(item)

        else:
            new_node.setPrevious(self.__tail)
            self.__tail.setNext(new_node)
            self.__tail = new_node

        self.__size += 1

    def insert(self, pos, item):
        assert isinstance(pos, int), ('Error: Type error: %s' % (type(pos))) # throws an assertion error on not true
        assert pos >= 0, ('Error: Illegal pos: %d' % (pos))

        new_node = DLinkedListNode(item,None,None)
        index = 1
        current = self.__head

        if pos == 1:
            self.add(item)
            
        elif pos > self.__size:
            self.append(item)
        
        else:
            while index!=pos:
                current = current.getNext()
                index+=1
                if index == pos:
                    break

            new_node.setNext(current)
            new_node.setPrevious(current.getPrevious())
            current.getPrevious().setNext(new_node)
            current.setPrevious(new_node)

            self.__size +=1
            
                

    def pop1(self):
        # removes and returns the last item in the list
        # save tail data to variable

        #method 1 use remove method to remove the node
        #OR
        #method 2 set the previous of tail to none... set next of previous of tail to none
        pass


    def pop(self, pos=None):
        #  removes and returns the item in the given position.
        # TODO
        pass

    def searchLarger(self, item):

        # TODO
        pass

    def getSize(self):
        return self.__size

    def getItem(self, pos):
        # returns the item at the given position.
        # TODO
        pass

    def __str__(self):
        # create the string representation of the linked list
        # TODO
        current = self.__head
        string = ''
        while current != None:
            string = string + str(current.getData())+'->'
            current = current.getNext()
        return string
        


def test():

    linked_list = DLinkedList()

    # is_pass = (linked_list.getSize() == 0)
    # assert is_pass == True, "fail the test"

    print(linked_list)

    linked_list.add("World")
    linked_list.add("Hello")
    linked_list.append("!")

    linked_list.insert(2,"!")

    # linked_list.remove("!")

    print(linked_list)


if __name__ == '__main__':
    test()

