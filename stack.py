
class Stack:
    def __init__(self): # stack() constructor
        self.__index = []

    def push(self, item): # adds an item to top of stack
        self.__index.append(item)

    def peek(self): # returns the top item of stack without removing it
       if not self.__index:
           raise IndexError("peek from empty stack")
       return self.__index[-1]

    def pop(self): # removes and returns the top item of stack
       if not self.__index:
           raise IndexError("pop from empty stack")
       return self.__index.pop()

    def is_empty(self): # returns True if stack is empty, False otherwise
       return not self.__index

    def size(self): # returns the number of items in the stack
        return len(self.__index)


    
