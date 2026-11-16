"""
Author: Preston Dahl 
Date: 2026-11-16
Lab: lab08
Last modified: 2026-11-16
Purpose: Makes every function is required to make a full Pokedex like add, search, print, copy, and remove.
"""

from pokedex_internals import Pokedex_internals
from pokemon import Pokemon


class pokedex_funcs:
    def __init__(self):
        self.pokedex_internals = Pokedex_internals()
        self.valid_traversals = ["pre", "in", "post", "pre-order", "in-order", "post-order", "preorder", "inorder", "postorder"]
        self.new_user_add = []
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #checking vailidity with respect to what is required like string in first entry, int in second entry, string in third entry, and only 3 entries
    def valid_pokemon(self, entry):
        try:
            for letter in entry[1]:
                if letter in self.alphabet:
                    return False

        except IndexError:
            return False
        
        if  (len(entry) < 3 or len(entry) > 3):
            return False
        
        if ((entry[0].isdigit() and entry[0].isascii()) or entry[0] == ""):
            print(entry[0])
            return False 
            
        if ((not entry[1].isdigit() and not entry[1].isascii()) or entry[1] == ""):
            return False
        
        if ((entry[2].isdigit() and entry[2].isascii()) or entry[2] == ""):
            return False
        
        return True

    def Add(self):
        prompt = "Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): "
        centered = prompt.center(146)
        clean = centered[:146 // 2 + len(prompt) // 2]
        user_add = input(f"|{clean}").lower().strip().split(",")

        while not self.valid_pokemon(user_add):
            prompt = "Enter valid Entries: "
            centered = prompt.center(146)
            # Keeps the first bracket in the line while also leaving the second bracket out to avoid wonkiness with input
            # I would have needed cursor control functions to fully create the full "Pokedex" effect
            clean = centered[:146 // 2 + len(prompt) // 2]
            user_add = input(f"|{clean}").lower().strip().split(",")

        # This was my fix for something like bee, 200, bee not working in my original BST submission
        self.new_user_add.clear()
        self.new_user_add.append(user_add[0].strip()) 
        self.new_user_add.append(user_add[1].strip()) 
        self.new_user_add.append(user_add[2].strip())

        try:
            # This was my workaround for checking if the copy had been created or not
            if self.pokedex_internals_copy.instance_created == True:
                # Prompts for copy or not
                print(f"|{f"".center(146)}|")
                prompt = "Which version of the Pokedex do you want to use (Copy or Original): "
                centered = prompt.center(146)
                clean = centered[:146 // 2 + len(prompt) // 2]
                user_input = input(f"|{clean}").lower().strip()
                print(f"|{f"".center(146)}|")
                print(f"|{f"Adding {self.new_user_add[0]}, {self.new_user_add[1]}, {self.new_user_add[2]}  to the {user_input} pokedex...".center(146)}|")
                print(f"|{"".center(146)}|")
                                            
                if user_input == "copy":
                    self.poke_copy = Pokemon(self.new_user_add[0], int(self.new_user_add[1]), self.new_user_add[2])
                    self.pokedex_internals_copy.add(self.poke_copy)                           

                    # This was my workaround for checking if the action had failed or not
                    if self.pokedex_internals_copy.Failed == True:
                        return
                        
                if user_input == "original":
                    self.poke_OG = Pokemon(self.new_user_add[0], int(self.new_user_add[1]), self.new_user_add[2])
                    self.pokedex_internals.add(self.poke_OG)
                    
                    if self.pokedex_internals.Failed == True:
                        return   
                                         
                print(f"|{f"{self.new_user_add[0]}, {self.new_user_add[1]}, {self.new_user_add[2]} added to the {user_input} Pokedex successfully.".center(146)}|")

        # Checking for an Attribute that doesn't exist prompts an AttributeError so I just used that for the no copy created section
        except AttributeError:                        
            self.poke_norm = Pokemon(self.new_user_add[0], int(self.new_user_add[1]), self.new_user_add[2])

            print(f"|{"".center(146)}|")                          
            print(f"|{f"Adding {self.new_user_add[0]}, {self.new_user_add[1]}, {self.new_user_add[2]} to the Pokedex...".center(146)}|")
            print(f"|{"".center(146)}|")
                
            self.pokedex_internals.add(self.poke_norm)
            
            if self.pokedex_internals.Failed == True:
                return
            
            print(f"|{f"{self.new_user_add[0]}, {self.new_user_add[1]}, {self.new_user_add[2]} added to the Pokedex successfully.".center(146)}|")

    # I used the same formatting with every function except copy which is at the bottom
    def search(self):
        prompt = "Enter a Pokemon ID to search for: "
        centered = prompt.center(146)
        clean = centered[:146 // 2 + len(prompt) // 2]
        user_search = input(f"|{clean}").strip()
        print(f"|{"".center(146)}|")

        try:
            if self.pokedex_internals_copy.instance_created == True:
                prompt = "Which version of the Pokedex do you want to use (Copy or Original): "
                centered = prompt.center(146)
                clean = centered[:146 // 2 + len(prompt) // 2]
                user_input = input(f"|{clean}").lower().strip()
                print(f"|{f"".center(146)}|")


                while user_input != "copy" and user_input != "original":
                    prompt = "Enter a vaild Pokedex version: "
                    centered = prompt.center(146)
                    clean = centered[:146 // 2 + len(prompt) // 2]
                    user_input = input(f"|{clean}").lower().strip()

                while not user_search.isascii() or not user_search.isdigit():
                    prompt = "Enter a valid Pokemon ID: "
                    centered = prompt.center(146)
                    clean = centered[:146 // 2 + len(prompt) // 2]
                    user_search = input(f"|{clean}").strip()

                print(f"|{f"Searching for Pokemon ID {user_search} in the {user_input} Pokedex...".center(146)}|")
                print(f"|{f"".center(146)}|")
                                   
                if user_input == "copy":
                    self.pokedex_internals_copy.search(int(user_search))
                    
                    if self.pokedex_internals_copy.Failed == True:
                        print(f"|{f"Pokemon ID {user_search} does not exist in the {user_input} Pokedex.".center(146)}|")
                        return

                if user_input == "original":
                    self.pokedex_internals.search(int(user_search))
                    if self.pokedex_internals.Failed == True:
                        print(f"|{f"Pokemon ID {user_search} does not exist in the {user_input} Pokedex.".center(146)}|")
                        return
                            
        except AttributeError:
            while not user_search.isdigit() or not user_search.isascii():
                user_search = input("Emter a valid Pokemon ID: ").strip()
            print(f"|{f"Searching for Pokemon ID {user_search}...".center(146)}|")
            print(f"|{"".center(146)}|")

            self.pokedex_internals.search(int(user_search))
            
            if self.pokedex_internals.Failed == True:
                print(f"|{f"Pokemon ID {user_search} does not exist in the Pokedex.".center(146)}|")
                return
            
    def print(self):
        prompt = "Enter a traversal method (post, in, pre): "
        centered = prompt.center(146)
        clean = centered[:146 // 2 + len(prompt) // 2]
        user_option = input(f"|{clean}").lower().strip()
        print(f"|{f"".center(146)}|")

        # Traversal option vailidity check
        while user_option not in self.valid_traversals:
            prompt = "Enter a valid Traversal Method: "
            centered = prompt.center(146)
            clean = centered[:146 // 2 + len(prompt) // 2]
            user_option = input(f"|{clean}").lower().strip()

        try:
            if self.pokedex_internals_copy.instance_created == True:
                prompt = "Which version of the Pokedex do you want to use (Copy or Original): "
                centered = prompt.center(146)
                clean = centered[:146 // 2 + len(prompt) // 2]
                user_input = input(f"|{clean}").lower().strip()
                print(f"|{f"".center(146)}|")

                while user_input != "copy" and user_input != "original":
                    prompt = "Enter a vaild Pokedex version: "
                    centered = prompt.center(146)
                    clean = centered[:146 // 2 + len(prompt) // 2]
                    user_input = input(f"|{clean}").lower().strip()

                print(f"|{f"Listing {user_input} Pokedex Entries...".center(146)}|")
                print(f"|{f"".center(146)}|")

                if user_input == "copy":
                    self.pokedex_internals_copy.visit_option(user_option)
         
                    if self.pokedex_internals_copy.Failed == True:
                        return
                    
                if user_input == "original":
                    self.pokedex_internals.visit_option(user_option)
         
                    if self.pokedex_internals.Failed == True:
                        return
                
                print(f"|{"".center(146)}|")
                print(f"|{f"{user_input} Pokedex Entries listed successfully.".center(146)}|")

        except AttributeError:
            print(f"|{f"Listing Pokedex Entries...".center(146)}|")
            print(f"|{f"".center(146)}|")
            
            self.pokedex_internals.visit_option(user_option)

            print(f"|{f"".center(146)}|")
            print(f"|{f"Pokedex Entries listed successfully.".center(146)}|")

    def remove(self):
        prompt = "Enter a Pokemon ID to remove: "
        centered = prompt.center(146)
        clean = centered[:146 // 2 + len(prompt) // 2]
        user_remove = input(f"|{clean}").strip()
        print(f"|{f"".center(146)}|")

        try:
            if self.pokedex_internals_copy.instance_created == True:
                prompt = "Which version of the Pokedex would you like to use (Copy or Original): "
                centered = prompt.center(146)
                clean = centered[:146 // 2 + len(prompt) // 2]
                user_input = input(f"|{clean}").lower().strip()
                print(f"|{f"".center(146)}|")

                while user_input != "copy" and user_input != "original":
                    prompt = "Enter a vaild Pokedex version: "
                    centered = prompt.center(146)
                    clean = centered[:146 // 2 + len(prompt) // 2]
                    user_input = input(f"|{clean}").lower().strip().split(",")

                print(f"|{f"Removing Pokemon ID {user_remove} from the {user_input} Pokedex...".center(146)}|")
                print(f"|{"".center(146)}|")

                if user_input == "copy":
                    self.pokedex_internals_copy.remove(int(user_remove))
         
                    if self.pokedex_internals_copy.Failed == True:
                        print(f"|{f"Pokemon ID {user_remove} does not exist in the {user_input} Pokedex.".center(146)}|")
                        return
                                          
                if user_input == "original":
                    self.pokedex_internals.remove(int(user_remove))
         
                    if self.pokedex_internals.Failed == True:
                        print(f"|{f"Pokemon ID {user_remove} does not exist in the {user_input} Pokedex.".center(146)}|")
                        return
                           
                print(f"|{f"Pokemon ID {user_remove} removed from the {user_input} Pokedex successfully.".center(146)}|")
                       
        except AttributeError:            
            print(f"|{f"Removing Pokemon ID {user_remove} from the Pokedex...".center(146)}|")
            print(f"|{f"".center(146)}|")

            self.pokedex_internals.remove(int(user_remove))
         
            if self.pokedex_internals.Failed == True:
                print(f"|{f"Pokemon ID {user_remove} does not exist in the Pokedex.".center(146)}|")
                return
            
            print(f"|{f"Pokemon ID {user_remove} removed from the Pokedex successfully.".center(146)}|")

    # A copy of the internal Pokedex gets created so now all of the functions now know to check to prompt for a copy or not
    def copy(self, pokemon):
        self.pokedex_internals_copy = Pokedex_internals()
        self._rec_copy(pokemon)

    # Used the pre-order traversal method to make a copy
    def _rec_copy(self, pokemon):
        if pokemon is not None:
            self.pokedex_internals_copy.add(pokemon.entry)
            self._rec_copy(pokemon.left)
            self._rec_copy(pokemon.right)
        