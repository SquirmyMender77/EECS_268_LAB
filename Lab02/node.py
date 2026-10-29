"""
Author: Preston Dahl
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Defines the Node class used to construct linked data structures like Stack.
"""

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None
