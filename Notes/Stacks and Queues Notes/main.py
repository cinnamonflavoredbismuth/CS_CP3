# CS Stacks and Queues Notes
"""
What is time complexity in programming?
    different amounts of mathing takes different amount of times. less things having to be done = faster time. big O notation
What are the levels of time complexity?
    O(1): standard time. search one thing in an array. no matter what happens I only use one algorithm. fastest. ideal
    O(n): linear time. direct correlation between size of data and how long itll take
    O(n log(n)): linear logarithmic. deals with most of sorting algorithms
    O^2: quadratic time. performs # of operations proportional to the square of the amount of input. inefficient. avoid this. bubble sort, select sort, insert sort
What is a stack?
    a type of list where you can only add to the top and remove from the top
What does LIFO stand for?
    last in first out
What are the things that a stack can do?
    you can use it for a deck of cards, search history, basically making it so you can only access one at a time
How are stacks normally written in python?
    with a stack class
What is a queue?
    A type of list basically
How are queues different from stacks?
    First in = first out for qeueus, Last in = First out stacks
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else: 
            return None
        
    def size(self):
        return len(self.items)
    
class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqeue(self,item): 
        self.items.append(item)

    def deqeue(self): 
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def peek(self): 
        if not self.is_empty():
            return self.items[0]
        else: 
            return None
        
    def size(self):
        return len(self.items)        
    