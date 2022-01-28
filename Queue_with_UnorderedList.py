# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:37:34 2022

@author: dcsem
"""

import UnorderedList

class Queue:
    
    '''Implementation of a queue using an unordered linked lists.
        The method enqueue takes constant time O(1), while the method
        dequeue takes linear time O(n), where n is the length of the queue.'''
    
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



