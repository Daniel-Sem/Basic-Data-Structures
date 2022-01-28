# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 10:09:54 2022

@author: dcsem
"""

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
    
    def set_data(self, data):
        
        self.data = data

    def set_next(self, next):
        
        self.next = next
        
    def get_data(self):
        
        return self.data
        
    def get_next(self):
        
        return self.next
    

class OrderedList:
    
    def __init__(self):
        
        self.head = None
        
    def add(self, data):
        '''Adds a new item to the list making sure that the order is preserved.
            It needs the item and returns nothing. Assume the item is not 
            already in the list.'''         
        
        current = self.head
        previous = None
        stop = False
        temp = Node(data)
        
        while current != None and not stop:
            
            if current.get_data() > data:
                stop = True
                
            else:
                previous = current
                current = current.get_next()
            
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
            
    
    def remove(self, rem_val):
        '''Removes the item from the list. It needs the item and modifies
            the list. Assume the item is present in the list.'''        
        
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            
            if current.get_data() == rem_val:
                stop = True
            
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
            
        else:
            previous.set_next(current.get_next())
            
    def search(self, data):
        '''Searches for the item in the list. It needs the item and returns
            a boolean value'''
        
        current = self.head
        stop = False
        
        while current != None and not stop:
            
            if current.get_data() == data:
                stop = True
            
            else:
                current = current.get_next()
        
        return stop
        
        
    def show(self):
        '''Prints all the items in the list within '...' sepatetors. Needs nothing
            and returns nothing'''
        
        current = self.head
            
        print('...')
        while current != None:
            print(current.get_data())
            current = current.get_next()
        print('...')
        
    def is_empty(self):
        '''Tests to see whether the list is empty. It needs no parameters and
            returns a boolean value.'''        
        
        if self.head == None:
            return True
        else:
            return False
        
    def size(self):
        '''Returns the number of items in the list. It needs no parameters and
            returns an integer.'''
        
        current = self.head
        count = 0
        
        while current != None:
            current = current.get_next()
            count += 1
            
        return count
    
    def index(self, data):
        '''Returns the position of item in the list. It needs the item and
            returns the index. Returns 'Item not found.' if the item is not
            in the list'''
        
        current = self.head
        count = 0
        stop = False
        
        while current != None and not stop:
            
            if current.get_data() == data:
                stop = True
            
            current = current.get_next()
            count += 1
        
        if current == None and not stop:
            return 'Item not found.'
        else:
            return count
        
    def pop(self):
        '''Removes and returns the last item in the list. It needs nothing and
            returns an item.'''
        
        current = self.head
        previous = None
        
        while current.get_next() != None:
            
            previous = current
            current = current.get_next()
        
        previous.set_next(None)
        
        return current.get_data()
    
            
# o_list = OrderedList()
# print(o_list.is_empty())

# o_list.add(34)
# o_list.add(23)
# o_list.add(31)
# o_list.add(11)
# o_list.add(1)
# o_list.add(21)
# o_list.add(12)
# o_list.add(66)
# o_list.add(4)      

# print('Size is: ', o_list.size())
# print(o_list.is_empty())
# o_list.show()         

# print(o_list.search(21))
# o_list.remove(11)
# o_list.remove(1)
# o_list.remove(21)
# print(o_list.search(21))
# print('Size is: ', o_list.size())
# o_list.show()      

# print(o_list.index(12))
# print(o_list.index(31))
# print(o_list.index(66))
# print(o_list.index(55))

# print(o_list.pop())
# print(o_list.pop())


# print('Size is: ', o_list.size())
# o_list.show()  

# o_list.add(111)
# o_list.add(2322)
# o_list.add(6)

# print('Size is: ', o_list.size())
# o_list.show()  

# • pop(pos) removes and returns the item at position pos. It needs the position and returns
# the item. Assume the item is in the list.
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    