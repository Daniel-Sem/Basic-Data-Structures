# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:36:50 2021

@author: dcsem
"""
class Stack:
    """ Instance of a Stack, implemented with a list, that pushes and pops from
    the last position in the list. That way both push and pop operations take constant time O(1)."""
    
    def __init__(self):
        
        self.elements = []
    
    def is_empty(self):
        
        return self.elements == []
    
    def push(self, item):
        
        self.elements.append(item)
        
    def pop(self):
        
        return self.elements.pop()
    
    def peek(self):
        
        return self.elements[len(self.elements)-1]
    
    def size(self):
        
        return len(self.elements)
    
    def show(self):
        
        print('...')        
        for i in self.elements:
            print(i)
        print('...')    
            
