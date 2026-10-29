"""
Author: Preston Dahl and a little of help on the index starter from Gemini 
Date: 2026-09-30
Lab: lab04
Last modified: 2026-09-30
Purpose: Implements a browser with navigation history using a linked list.
"""
from linkedlist import linkedlist

class Browser:
    def __init__(self):
        self.linked = linkedlist(None)
        self.current_index = -1

    def navigate(self, entry):
        while self.current_index + 1 < self.linked._length:
            self.linked.remove(self.current_index + 1)

        self.linked.insert(self.linked._length, entry)
        self.current_index = self.linked._length - 1

    def back(self):
        if self.current_index <= 0:
            return None

        self.current_index -= 1
        entry = self.linked.get_entry(self.current_index)
        return entry

    def forward(self):
        if self.current_index >= self.linked._length - 1:
            return None

        self.current_index += 1
        entry = self.linked.get_entry(self.current_index)
        return entry

    def history(self):
        print("Oldest\n==================")
        for i in range(self.linked._length):
            entry = self.linked.get_entry(i)
            marker = "  <==current" if self.current_index == i else ""
            print(f"{entry}{marker}")
        print("==================\nNewest\n")
