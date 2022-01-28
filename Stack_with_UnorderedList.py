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




