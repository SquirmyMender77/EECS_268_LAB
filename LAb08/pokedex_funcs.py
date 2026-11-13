from pokedex_internals import Pokedex_internals
from pokemon import Pokemon


class pokedex_funcs:
    def __init__(self):
        self.pokedex_internals = Pokedex_internals()
        self.valid_traversals = ["pre", "in", "post", "pre-order", "in-order", "post-order", "preorder", "inorder", "postorder"]

    def valid_pokemon(self, entry):
        if len(entry) < 3 or len(entry) > 3 or not entry[1].isascii() or not entry[1].isdigit() or entry[0] == "" or entry[1] == "" or entry[2] == "":
            return False
        
        else:
            return True

    def Add(self):
        user_add = input("Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): ")
        user_add = user_add.lower()
        user_add = user_add.split(",")
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                while not self.valid_pokemon(user_add):
                    user_add = input("Invalid input, please try again: ")
                    user_add = user_add.lower()
                    user_add = user_add.split(",")
                                
                else:
                    if user_input == "copy":
                        self.poke_copy = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"                          
                             f"Adding {user_add[0]},{user_add[1]},{user_add[2]} to the pokedex...")
                        self.pokedex_internals_copy.add(self.poke_copy)

                    if user_input == "original":
                        self.poke_OG = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"                          
                        f"Adding {user_add[0]},{user_add[1]},{user_add[2]}  to the pokedex...")
                        self.pokedex_internals.add(self.poke_OG)

        except AttributeError:
            while not self.valid_pokemon(user_add):
                user_add = input("Invalid input, please try again: ")
                user_add = user_add.lower()
                user_add = user_add.split(",")

            else:
                self.poke_norm = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"                          
                     f"Adding {user_add[0]},{user_add[1]},{user_add[2]} to the pokedex...")
                self.pokedex_internals.add(self.poke_norm)
                

    def search(self):
        user_search = input("Enter a Pokemon ID to search for: ")
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()

                while not user_search.isascii() or not user_search.isdigit():
                    user_search = input("Enter a valid pokedex ID: ")
                
                if user_input == "copy":
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                         f"Searching for ID {user_search}...")
                    self.pokedex_internals_copy.search(int(user_search))

                if user_input == "original":
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                         f"Searching for ID {user_search}...")
                    self.pokedex_internals.search(int(user_search))

        except AttributeError:
            while not user_search.isdigit() or not user_search.isascii():
                user_search = input("Emter a valid pokedex ID: ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                     f"Searching for ID {user_search}...")
            self.pokedex_internals.search(int(user_search))
            
    def print(self):
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_option = input("Enter a traversal method (post, in, pre): ")
                user_option = user_option.lower()
                while user_option not in self.valid_traversals:
                    user_option = input("Enter a valid Traversal Method: ")
                    user_option = user_option.lower()

                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()

                if user_input == "copy":
                    self.pokedex_internals_copy.visit_option(user_option)

                if user_input == "orginal":
                    self.pokedex_internals.visit_option(user_option)

        except AttributeError:
            user_option = input("Enter a traversal method (post, in, pre): ")
            user_option = user_option.lower()
            while user_option not in self.valid_traversals:
                user_option = input("Enter a valid Traversal Method: ")
                user_option = user_option.lower()
            self.pokedex_internals.visit_option(user_option)

    def remove(self):
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the Tree would you like to use (Copy or Original): ")
                user_input = user_input.lower()
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()
            
                if user_input == "copy":
                    user_input = input("Enter a Pokemon ID to remove: ")
                    self.pokedex_internals_copy.remove(int(user_input))
            
                if user_input == "original":
                    user_input = input("Enter a Pokemon ID to remove: ")
                    self.pokedex_internals.remove(int(user_input))

        except AttributeError:
            user_input = input("Enter a pokemon ID: ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  f"Removing ID {user_input}")
            self.pokedex_internals.remove(int(user_input))

    def copy(self, pokemon):
        self.pokedex_internals_copy = Pokedex_internals()
        self._rec_copy(pokemon)

    def _rec_copy(self, pokemon):
       if pokemon is not None:
            self.pokedex_internals_copy.no_text_add(pokemon.entry)
            self._rec_copy(pokemon.left)
            self._rec_copy(pokemon.right)
        
