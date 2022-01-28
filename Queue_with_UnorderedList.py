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

