from pokedex_internals import Pokedex_internals
from pokemon import Pokemon


class pokedex_funcs:
    def __init__(self):
        self.pokedex_internals = Pokedex_internals()

    def Add(self, comparison_file):
        try:
            try:
                if self.pokedex_internals_copy.instance_created == True:
                    user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                    user_input = user_input.lower()
                    user_add = input("Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): ")
                    user_add = user_add.lower()
                    user_add = user_add.split(",")
                    while len(user_add) < 3 or len(user_add) > 3 or not user_add[1].isascii() or not user_add[1].isdigit():
                        user_add = input("Invalid input, please try again: ")
                        user_add = user_add.lower()
                        user_add = user_add.split(",")
                                
                    for line in comparison_file:
                        print(user_add[0])
                        print(line[0])
                        if user_add[0] == line[0]:
                            user_add = input("Entry already exists, please try again: ")
                            user_add = user_add.lower()
                            user_add = user_add.split(",")

                    for line in comparison_file:
                        print(user_add[1])
                        print(line[1])
                        if user_add[1] == line[1]:
                            user_add = input("Entry already exists, please try again: ")
                            user_add = user_add.lower()
                            user_add = user_add.split(",")

                    for line in comparison_file:
                        print(user_add[2])
                        print(line[2])
                        if user_add[2] == line[2]:
                            user_add = input("Entry already exists, please try again: ")
                            user_add = user_add.lower()
                            user_add = user_add.split(",")

                    else:
                        if user_input == "copy":
                            self.poke = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                            self.pokedex_internals_copy.add(self.poke)

                        if user_input == "original":
                            self.poke = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                            self.pokedex_internals.add(self.poke)

            except IndexError:
                print("Not enough entries, please try again.")
                self.Add(comparison_file)

        except AttributeError:
            try:
                user_add = input("Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): ")
                user_add = user_add.lower()
                user_add = user_add.split(",")
                while len(user_add) < 3 or len(user_add) > 3 or not user_add[1].isascii() or not user_add[1].isdigit():
                    user_add = input("Invalid input, please try again: ")
                    user_add = user_add.lower()
                    user_add = user_add.split(",")

                for line in comparison_file:
                    if user_add[0] == line[0]:
                        user_add = input("Entry already exists, please try again: ")
                        user_add = user_add.lower()
                        user_add = user_add.split(",")

                for line in comparison_file:
                    if user_add[1] == line[1]:
                        user_add = input("Entry already exists, please try again: ")
                        user_add = user_add.lower()
                        user_add = user_add.split(",")

                for line in comparison_file:
                    if user_add[2] == line[2]:
                        user_add = input("Entry already exists, please try again: ")
                        user_add = user_add.lower()
                        user_add = user_add.split(",")
                        
                else:
                    self.poke = Pokemon(user_add[0], int(user_add[1]), user_add[2])
                    self.pokedex_internals.add(self.poke)

            except IndexError:
                print("Not enough entries, please try again.")
                self.Add(comparison_file)

    def search(self):
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_search = input("Enter a Pokemon ID to search for: ")
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()
                
                if user_input == "copy":
                    self.poke = Pokemon(self.pokedex_internals_copy.current_A_name, self.pokedex_internals_copy.current_ID, self.pokedex_internals_copy.current_J_name)
                    self.pokedex_internals_copy.search(self.pokedex_internals_copy.root, int(user_search))

                if user_input == "original":
                    self.poke = Pokemon(self.pokedex_internals.current_A_name, self.pokedex_internals.current_ID, self.pokedex_internals.current_J_name)
                    self.pokedex_internals.search(self.pokedex_internals.root, int(user_search))

        except AttributeError:
            user_input = input("Enter a pokedex ID: ")
            self.poke = Pokemon(self.pokedex_internals.current_A_name, self.pokedex_internals.current_ID, self.pokedex_internals.current_J_name)
            self.pokedex_internals.search(self.pokedex_internals.root, int(user_input))
            
    def print(self):
        try:
            if self.pokedex_internals_copy.instance_created == True:
                user_input = input("Which version of the tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_option = input("Enter a traversal method (post, in, pre): ")
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
            self.pokedex_internals.visit_option(user_option.lower())

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
                    self.pokedex_internals_copy.remove(1, int(user_input))
            
                if user_input == "original":
                    user_input = input("Enter a Pokemon ID to remove: ")
                    self.pokedex_internals.remove(1, int(user_input))

        except AttributeError:
            user_input = input("Enter a pokemon ID: ")
            self.pokedex_internals.remove(1, int(user_input))

    def copy(self, OG_file):
        self.pokedex_internals_copy = Pokedex_internals()
        for line in OG_file:
            self.pokedex_internals_copy.add(int(line[1]))
