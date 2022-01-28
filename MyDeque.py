# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:03:53 2021

@author: dcsem
"""

class Deque:
    
    """Instance of the Deque ADT, implemented with a list."""
    
    def __init__(self):
        
        self.items = []
        
    def is_empty(self):
        
        return self.items == []
    
    def size(self):
        
        return len(self.items)
    
    def add_rear(self, item):
        
        self.items.insert(0, item)
        
    def add_frond(self, item):
        
        self.items.append(item)
        
    def remove_rear(self):
        
        return self.items.pop(0)
    
    def remove_frond(self):

        return self.items.pop()
        

        
        
        
        
        
        
        
        
        