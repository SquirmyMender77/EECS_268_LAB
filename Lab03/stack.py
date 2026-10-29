"""
Author: Preston Dahl
KUID: [ID REDACTED]
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Implements a node-based stack with push, pop, peek, and is_empty methods.
"""

from node import Node

class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self._top
        self._top = new_node

    def pop(self):
        if self.is_empty():
            raise RuntimeError("pop from empty stack")
        popped = self._top.entry
        self._top = self._top.next
        return popped
    
    def peek(self):
        if self.is_empty():
            raise RuntimeError("peek from empty stack")
        return self._top.entry
    
    def is_empty(self):
        return self._top is None
