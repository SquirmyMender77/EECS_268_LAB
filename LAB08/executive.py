from BST import BST

class executive:
    def __init__(self):
        self.bst = BST()

    def Add(self, american_names, pokedex_IDs, japanese_names):
        try:
            if self.bst_copy.instance_created == True:
                user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_add = input("Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): ")
                user_add = user_add.lower()
                user_add = user_add.split(",")
                while user_add[0] in american_names  or user_add[1] in pokedex_IDs or user_add[2] in japanese_names:
                    user_add = ("Entry already exists, please try again: ")
                    user_add = user_add.lower()
                    user_add = user_add.split(",")
                                
                else:
                    while len(user_add) < 3 or len(user_add) > 3:
                        user_add = input("Invalid input, please try again: ")
                        user_add = user_add.lower()
                        user_add = user_add.split(",")

                    if user_input == "copy":
                        self.bst_copy.add(user_add)

                    if user_input == "original":
                        self.bst.add(user_add)

        except AttributeError:
            user_add = input("Enter an American Pokemon Name, Pokedex ID Number, and Japanese Pokemon Name (comma-separated if you'd be so kind): ")
            user_add = user_add.lower()
            user_add = user_add.split(",")
            while user_add[0] in american_names  or user_add[1] in pokedex_IDs or user_add[2] in japanese_names:
                user_add = ("Entry already exists, please try again: ")
                user_add = user_add.lower()
                user_add = user_add.split(",")
                    
            else:
                while len(user_add) < 3 or len(user_add) > 3:
                    user_add = input("Invalid input, please try again: ")
                    user_add = user_add.lower()
                    user_add = user_add.split(",")

                self.bst.add(user_add)

    def search(self, OG_file, pokedex_IDs, american_names, japanese_names):
        try:
            if self.bst.instance_created == True:
                user_input = input("Which version of the Tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_search = input("Enter a Pokemon ID to search for: ")
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()
                
                if user_input == "copy":
                    self.bst_copy.search(user_search)

                if user_input == "original":
                    self.bst.search(user_search)

        except AttributeError:
            user_input = input("Enter a pokedex ID: ")
            self.bst.search(user_input)
            
    def print(self):
        try:
            if self.bst_copy.instance_created == True:
                user_input = input("Which version of the tree do you want to use (Copy or Original): ")
                user_input = user_input.lower()
                user_option = input("Enter a traversal method (post, in, pre): ")
                user_option = user_option.lower()
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()

                if user_input == "copy":
                    self.bst_copy.visit_option(user_option)

                if user_input == "orginal":
                    self.bst.visit_option(user_option)

        except AttributeError:
            user_option = input("Enter a traversal method (post, in, pre): ")
            self.bst.visit_option(user_option.lower())

    def remove(self):
        try:
            if self.bst_copy.instance_created == True:
                user_input = input("Which version of the Tree would you like to use (Copy or Original): ")
                user_input = user_input.lower()
                while user_input != "copy" and user_input != "original":
                    user_input = input("Enter a vaild Tree version: ")
                    user_input = user_input.lower()
            
                if user_input == "copy":
                    user_input = input("Enter a Pokemon ID to remove: ")
                    self.bst_copy.remove(user_input)
            
                if user_input == "original":
                    user_input = input("Enter a Pokemon ID to remove: ")
                    self.bst.remove(user_input)

        except AttributeError:
            user_input = input("Enter a pokemon ID: ")
            self.bst.remove(user_input)
            print(f"{user_input} removed")

    def copy(self, OG_file):
        self.bst_copy = BST()
        for line in OG_file:
            self.bst_copy.add(line[1])
