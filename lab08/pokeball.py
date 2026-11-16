"""
Author: Preston Dahl 
Date: 2026-12-16
Lab: lab08
Last modified: 2026-11-16
Purpose: Pokeball class that stores Pokemon in the Pokedex.
"""

class Pokeball:
# Same as last LAB except with a new name
    def __init__(self, entry):
        self.entry = entry
        self.right = None
        self.left = None
