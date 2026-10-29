"""
Author: Preston Dahl and help from Gemini on the insert function
Date: 2026-09-30
Lab: lab04
Last modified: 2026-09-30
Purpose: Implements a singly linked list data structure.
"""
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class linkedlist:
    def __init__(self, current_node):
        self._front = None
        self._length = 0
        self.current_node = current_node

    def __len__(self):
        return self._length
    
    def clear(self):
        self._length = 0
        self._front = None
    
    def get_entry(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("index is out of range")

        self.current_node = self._front
        for i in range(index):
            self.current_node = self.current_node.next
        return self.current_node.entry
        

    def set_entry(self, index, entry):
        if index < 0 or index >= self._length:
            raise IndexError("index is out of range")

        self.current_node = self._front
        for i in range(index):
            self.current_node = self.current_node.next
        self.current_node.entry = entry

    def insert(self, index, entry):
        self.current_node = self._front
        self.index = index
        if index < 0 or index > self._length:
            raise IndexError("index is out of range")
        
        new_node = Node(entry)
        if index == 0:
            new_node.next = self._front
            self._front = new_node

        else:
            self.current_node = self._front
            for i in range(index - 1):
                self.current_node = self.current_node.next
            new_node.next = self.current_node.next
            self.current_node.next = new_node
        self._length += 1

    def remove(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("index is out of range")

        if index == 0:
            self._front = self._front.next
        else:
            self.current_node = self._front
            for i in range(index - 1):
                self.current_node = self.current_node.next
            self.current_node.next = self.current_node.next.next
        self._length -= 1