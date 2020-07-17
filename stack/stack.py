"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('../singly_linked_list')
import sys
import os, sys


from singly_linked_list import LinkedList, Node

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def push(self, value):
        # size of LL gets increased by 1 every time we push
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        # check if LL is empty. If so, we cannot remove an element
        if self.size == 0:
            return None
        # if not empty, remove the tail (LIFO) and decrase the size by 1
        else:
            self.size -= 1
            return self.storage.remove_tail()