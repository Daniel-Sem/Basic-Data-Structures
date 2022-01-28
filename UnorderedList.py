# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:39:39 2021

@author: dcsem
"""

class Node:
    
    '''The node objects hold the payload and a reference to the next node.'''
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
    
    def get_data(self):
        
        return self.data
    
    def get_next(self):
        
        return self.next
    
    def set_data(self, new_data):
        
        self.data = new_data
        
    def set_next(self, next_node):
        
        self.next = next_node
        
    
    
class UnorderedList:
    
    """An instance of Unordered list ADT, build with Node objects.
        Methods add and append take constant time O(1). Methods pop, insert,
        search and remove take linear time O(n), because of the traversal process."""
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
       """Checks if the lsit is empty, returns bool."""
       return self.head == None

    def add(self, item):
        """Adds given value to the list."""
        if self.size == 1:
            self.tail = self.head
            
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.size = self.size + 1

    def size_of_list(self):
        """Returns integer with the size of the list.""" 
        # current = self.head
        # count = 0
        
        # while  current != None:
        #     count +=1
        #     current = current.get_next()
            
        # return count
        
        return self.size
    
    def search(self, search_val):
        """Searches given value in the list."""      
        current = self.head 
        found = False
        
        while current != None and not found:
            
            if current.get_data() == search_val:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, rem_val):
        """Removes given value from the list."""
        current = self.head
        previous = None
        found = False
        Not_available = False
        
        while not Not_available:
            
            if current.get_data() == rem_val:
                found = True
                if previous == None:
                    self.head = current.get_next()
                    current = self.head
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()   
                self.size = self.size - 1
                
            else:
                if not Not_available:    
                    previous = current
                    current = current.get_next()
            if current.get_next() == None:
                    Not_available = True
                    if found == False:
                        print('Item', rem_val ,'not in list.')
        
    
    def append(self, new_data):
        """Appends given value to the end of the list using a pointer, that shows
           the last value is O(1) time."""
        temp = Node(new_data)
          
        if self.head == None:
            self.head = Node(new_data)
            self.tail = self.head
        
        else:
            self.tail.set_next(temp)
            self.tail = temp
            
        self.size += 1
                       
     
    def insert(self, new_data, pos):
        """Use to insert a given value on a given position in the list."""  
        current = self.head
        
        for item in range(pos-1):
            current = current.get_next()
            
        new_next = current.get_next()
        new_node = Node(new_data)
        new_node.set_next(new_next)
        current.set_next(new_node)
        self.size += 1
     
    def index(self, data):
        """Finds the index of a given value from the list. Returns 'Not found' 
            if the value is not in the list"""
        current = self.head
        count = 0
        found = False
        indices = []

        while current != None:
            if current.get_data() == data:
                indices.append(count)
                found = True

            current = current.get_next()
            count += 1
                   
        if found:
            return indices
        else:
            return "Not found"
     
     
    def pop(self):
        """Pops a value from the list."""
        current = self.head
        previous = None
        
        while current.get_next() != None:
                
            previous = current
            current = current.get_next()
            
        self.tail = previous
        if previous != None:
            previous.set_next(None)
        self.size -= 1
        return current.get_data()
    
    def pop_pos(self, pos):
        """Pops a value from the list by given position."""
        current = self.head
        previous = None
        found = False
        count = 0
        
        while current.get_next() != None and not found:
            
            if count == pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                count += 1
            
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.size -= 1
            return current.get_data()
        else:
            return 'Item not found'
    
    def show(self):
        """Prints the whole unordered list."""
        current = self.head
        print('...')
        while current.get_next() != None:
            print(current.get_data())
            current = current.get_next()
            
        print(current.get_data())
        print('...')
    
    def __str__(self):
        """Returns a string with the whole unordered list."""
        current = self.head
        ret_srt = []
        while current != None:
            ret_srt.append(current.get_data())
            current = current.get_next()
                    
        return str(ret_srt)
    
    def slice(self, start, end):
        """Takes two indices as start(inclusive) and end(exclusive) of the slice.
            Returns slice of the list"""
        
        current = self.head
        slice_list = UnorderedList()
        count = 0
        
        while current != None:
            
            if count >= start and count <= end:
                slice_list.add(current.get_data())
                
            current = current.get_next()
            count +=1
        
        return slice_list
            
                
    
