# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 09:12:48 2022

@author: dcsem
"""

class Node:
    '''In this implementation of a doubly linked list each node has a reference to the next node
    as well as a reference to the preceding node. The head reference also contains two references,
    one to the first node in the linked list and one to the last.'''
    def __init__(self, data):
        
        self.data = data
        self.next = None
        self.back = None
        
    def set_data(self, data):
        
        self.data = data
        
    def set_next(self, next_node):
        
        self.next = next_node

    def set_back(self, previous_node):
        
        self.back = previous_node
        
    def get_data(self):
        
        return self.data
    
    def get_next(self):
        
        return self.next
    
    def get_back(self):
        
        return self.back

class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None


    def add(self, item):
        """Adds a new item to the list. It needs the item and returns nothing.
            Assume the item is not already in the list."""   
        
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
            
        else:
            next_node = self.head
            current = Node(item)
            current.set_next(next_node)
            self.head = current
            next_node.set_back(self.head)
            
        
        # current = self.head
        # previous = None
        # while current != None:
        #     previous = current
        #     current = current.get_next()
            
        # if self.head == None:
            
        #     self.head = Node(item)
            
        # else:
            
        #     current = Node(item)
            
        #     previous.set_next(current)
        #     current.set_back(previous)
        #     self.tail = current

    
    def remove(self, item):
        '''Removes the given item from the list. It needs the item and modifies the
            list. Assumes the item is present in the list.'''
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() == item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        if not stop:
            print("Item not found.")
        else:
            
            if previous != None:
                previous.set_next(current.get_next())
            
            if current.get_next() != None:
                next_node = current.get_next()
                next_node.set_back(previous)
                
            if current.get_next() == None:
                previous.set_next(None)
                self.tail = previous
                
            
    def show(self):
        '''Print the contents of the list suraunded by '...'. It needs no arguments
            and returns nothing.'''
        
        current = self.head

        print('...')
        while current != None:
            print(current.get_data())
            current = current.get_next()
        print('...')
        
    def size(self):
        '''Returns the size of the list. It takes no arguments.'''        
        current = self.head
        count = 0

        while current != None:
            current = current.get_next()
            count +=1
        return count
    
    def search(self, item):
        '''Searches for the item in the list. It needs the item and returns
            a boolean value.'''
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            current = current.get_next()

        return found
                
    def is_empty(self):
        '''Tests to see whether the list is empty. It needs no parameters and
        returns a boolean value.'''
        
        if self.head == None:
            return True
        else:
            return False
    
    def append(self, item):
        '''Adds a new item to the end of the list making it the last item in
            the collection. It needs the item and returns nothing. Assume the
            item is not already in the list.'''
        
        if self.tail != None:
            current = self.tail
            new_node = Node(item)
            new_node.set_back(current)
            current.set_next(new_node)
            self.tail = new_node
        
        else:
            self.head = Node(item)
            self.tail = self.head

    def index(self, item):
        '''Returns the position of item in the list. It needs the item and
            returns the index. Assume the item is in the list.'''
    
        current = self.head
        count = 0
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                count +=1
                
        return count

    def insert(self, pos, item):
        '''Adds a new item to the list at position pos. It needs the item and
        returns nothing. Assume the item is not already in the list and
        there are enough existing items to have position pos.'''
        
        current = self.head
        count = 0

        
        while current != None and count != pos:
            current = current.get_next()
            count +=1
        
        if current == None:
            print('Index is out of bound.')
            
        else:
            new_node = Node(item)
            previous = current.get_back()
            previous.set_next(new_node)
            next_node = current
            next_node.set_back(new_node)
            new_node.set_next(next_node)

    def pop(self):
        '''Removes and returns the last item in the list. It needs nothing and
            returns an item. Assume the list has at least one item.'''
        current = self.tail
        previous = self.tail.get_back()
        previous.set_next(None)
        self.tail = previous
        
        return current.get_data()
        
    def pop_pos(self, pos):
        '''Removes and returns the item at position pos. It needs the position
            and returns the item. Assume the item is in the list'''
        
        current = self.head
        previous = None
        count = 0
        
        while current != None and count != pos:
            previous = current
            current = current.get_next()
            count +=1
                   
        if previous != None:
            previous.set_next(current.get_next())
            
        if current.get_next() != None:
            next_node = current.get_next()
            next_node.set_back(previous)
                
        if current.get_next() == None:
            previous.set_next(None)
            self.tail = previous
        
        return current.get_data()
    
    
    
