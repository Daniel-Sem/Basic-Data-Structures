# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:03:53 2021

@author: dcsem
"""

class Deque:
    
    """Instance of the Deque ADT, implemented with a list.
        Methods add_frond and remove from take constant time O(1), while methods add_rear
        and remove_rear from take linear time O(n), where n is the length of the data."""
    
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
        

