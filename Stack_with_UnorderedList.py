# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:25:40 2022

@author: dcsem
"""

# 20. Implement a stack using linked lists.

import UnorderedList

class Stack:
    
    def __init__(self):
        
        self.items = UnorderedList.UnorderedList()
        
    def push(self, item):
        
        self.items.append(item)
    
    def pop(self):
        
        return self.items.pop()
    
    def size(self):
        
        return self.items.size_of_list()
        
    def is_empty(self):
        
        return self.items.is_empty()
    
    def show(self):
        
      return print(self.items)


# pop
# push
# size
# is_empty
# print

# s = Stack()

# print(s.is_empty())
# s.push(23)
# s.push(11)
# s.push(22)
# s.push(55)
# s.push(33)
# s.push(56)
# s.push(18)
# s.push(71)
# s.push(64)
# s.push(2)
# print(s.is_empty())
# s.show()
# print(s.size())

# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

# s.show()
# print(s.size())

# s.push(56)
# s.push(18)
# s.push(71)

# s.show()
# print(s.size())

# print(s.pop())
# print(s.pop())

# s.show()
# print(s.size())
