"""
Author: Preston Dahl
Date: 2026-09-17
Lab: lab02
Last modified: 2026-09-17
Purpose: Represents a Function object containing its name and exception handling capabilities.
"""

class Function:
    def __init__(self, name, can_handle_exceptions=False):
        self.name = name
        self.can_handle_exceptions = can_handle_exceptions