# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:16:20 2021

@author: dcsem
"""

class Queue: 
    """Instance of the Queue ADT, implemented with a list, which enqueues from
    the beggining and dequeues from the last item of the list."""
    def __init__(self):
        
        self.items = []
        
    def is_empty(self):
        
        return self.items == []
    
    def enqueue(self, item):
        
        self.items.insert(0, item)
        
    def dequeue(self):
        
        return self.items.pop()
    
    def size(self):
        
        return len(self.items)
    
    def show(self):
        print('...')
        for item in self.items:
            print(item)
        print('...')



