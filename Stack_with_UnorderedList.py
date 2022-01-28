# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:25:40 2022

@author: dcsem
"""

import UnorderedList

class Stack:
    '''Implementation of a Stack ADT using unordered linked list. The method push takes O(1) time,
        while the method pop takes linear time O(n), where n is the length of the stack.'''
    
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




