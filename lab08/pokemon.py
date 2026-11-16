"""
Author: Preston Dahl 
Date: 2026-11-16
Lab: lab08
Last modified: 2026-11-16
Purpose: Pokemon class that allows the ID of the Pokemon to be compared for improved sorting, and a vaild entry when printed.
"""

class Pokemon:
    def __init__(self, cur_a_name, cur_poke_id, cur_j_name):
        # Current names and ID are thrown in to use for various methods
        self.a_name = cur_a_name
        self._id = cur_poke_id
        self.j_name = cur_j_name

    # Using self and other along with isinstance, I was able to compare ID's
    def __lt__(self, other):
        if isinstance(other, Pokemon):
            return self._id < other._id

        if isinstance(other, int):
            return self._id < other

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Pokemon):
            return self._id > other._id

        if isinstance(other, int):
            return self._id > other

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return self._id == other._id

        if isinstance(other, int):
            return self._id == other

        return NotImplemented

    # Str that is returned when printed
    def __str__(self):
        return(f"{self.a_name}, {self._id}, {self.j_name}")
