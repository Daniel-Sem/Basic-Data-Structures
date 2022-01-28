# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:37:34 2022

@author: dcsem
"""

# 21. Implement a queue using linked lists.

import UnorderedList

class Queue:
    
    def __init__(self):
        
        self.items = UnorderedList.UnorderedList()
        
    def enqueue(self, item):
        
        self.items.add(item)
    
    def dequeue(self):
        
        return self.items.pop()
    
    def size(self):
        
        return self.items.size_of_list()
        
    def is_empty(self):
        
        return self.items.is_empty()
    
    def show(self):
        
      return print(self.items)


# enqueue
# dequeue
# size
# is_empty
# print

# s = Queue()

# print(s.is_empty())
# s.enqueue(23)
# s.enqueue(11)
# s.enqueue(22)
# s.enqueue(55)
# s.enqueue(33)
# s.enqueue(56)
# s.enqueue(18)
# s.enqueue(71)
# s.enqueue(64)
# s.enqueue(2)
# print(s.is_empty())
# s.show()
# print(s.size())

# print(s.dequeue())
# print(s.dequeue())
# print(s.dequeue())
# print(s.dequeue())
# print(s.dequeue())

# s.show()
# print(s.size())

# s.enqueue(23)
# s.enqueue(11)
# s.enqueue(22)
# s.enqueue(55)

# s.show()
# print(s.size())

# print(s.dequeue())
# print(s.dequeue())

# s.show()
# print(s.size())
