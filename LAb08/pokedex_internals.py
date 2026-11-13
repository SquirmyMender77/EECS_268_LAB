from pokeball import Pokeball
from pokemon import Pokemon

class Pokedex_internals:
    def __init__(self):
        Pokedex_internals.instance_created = True
        self.root = None
        self.current_A_name = None
        self.copy_file = []
        self.current_ID = None
        self.current_J_name = None        

    def no_text_add(self, entry):
        new_pokemon = Pokeball(entry)
        if self.root is None:
            self.root = new_pokemon
        else:
            self._no_text_add_recursive(self.root, new_pokemon)
    
    def _no_text_add_recursive(self, current_pokemon, new_pokemon):
        if new_pokemon.entry < current_pokemon.entry:
            if current_pokemon.left is None:
                current_pokemon.left = new_pokemon
                
            else:
                self._no_text_add_recursive(current_pokemon.left, new_pokemon)

        if new_pokemon.entry > current_pokemon.entry:
            if current_pokemon.right is None:
                current_pokemon.right = new_pokemon


            else:
                self._no_text_add_recursive(current_pokemon.right, new_pokemon)

        if new_pokemon.entry == current_pokemon.entry:
            return

    def add(self, entry):
        new_pokemon = Pokeball(entry)
        if self.root is None:
            self.root = new_pokemon
        else:
            self._add_recursive(self.root, new_pokemon)

    def _add_recursive(self, current_pokemon, new_pokemon):
        if new_pokemon.entry < current_pokemon.entry:
            if current_pokemon.left is None:
                current_pokemon.left = new_pokemon
                print(f"{new_pokemon.entry} added to the Pokedex")
                return
                
            else:
                self._add_recursive(current_pokemon.left, new_pokemon)

        if new_pokemon.entry > current_pokemon.entry:
            if current_pokemon.right is None:
                current_pokemon.right = new_pokemon
                print(f"{new_pokemon.entry} added to the Pokedex")
                return


            else:
                self._add_recursive(current_pokemon.right, new_pokemon)

        if new_pokemon.entry == current_pokemon.entry:
            print(f"Failed to add {new_pokemon.entry} to the Pokedex due to a Duplication Error")
            return


    def _pre_order_recursive(self, pokemon):
        if pokemon is not None:
            print(pokemon.entry)
            self._pre_order_recursive(pokemon.left)
            self._pre_order_recursive(pokemon.right)

    def _in_order_recursive(self, pokemon):
        if pokemon is not None:
            self._in_order_recursive(pokemon.left)
            print(pokemon.entry)
            self._in_order_recursive(pokemon.right)

    def _post_order_recursive(self, pokemon):
        if pokemon is not None:
            self._post_order_recursive(pokemon.left)
            self._post_order_recursive(pokemon.right)
            print(pokemon.entry)        

    def visit_option(self, option):
        if option == "pre" or option == "pre-order" or option == "preorder":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Printing Entries:\n")
            self._pre_order_recursive(self.root)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Entries printed successfully.")

        if option == "in" or option == "in-order" or option == "inorder":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Printing Entries:\n")
            self._in_order_recursive(self.root)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Entries printed successfully.")

        if option == "post" or option == "post-order" or option == "postorder":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Printing Entries:\n")
            self._post_order_recursive(self.root)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Entries printed successfully.")
    
    def remove(self, key):
        self.root = self._rec_remove(self.root, key)
        
    def _rec_remove(self, current_pokemon, key):
        if current_pokemon == None:
            print(f"Pokemon ID {key} does not exist")
            return

        if key > current_pokemon.entry:
            current_pokemon.right = self._rec_remove(current_pokemon.right, key)
            return current_pokemon

        if key < current_pokemon.entry:
            current_pokemon.left = self._rec_remove(current_pokemon.left, key)
            return current_pokemon

        if current_pokemon.entry == key:
            temp = current_pokemon
            if temp.right == None and temp.left != None:
                print(f"{temp.left.entry} removed")
                return temp.left

            if temp.right != None and temp.left == None:
                print(f"{temp.right.entry} removed")
                return temp.right

            if temp.right == None and temp.left == None:
                print(f"{temp.entry} removed")
                return None

            if temp.right != None and temp.left != None:
                temp = current_pokemon.left
                while temp.right is not None:
                    temp = temp.right
                current_pokemon.entry = temp.entry
                current_pokemon.left = self._rec_remove(current_pokemon.left, current_pokemon.entry)
                print(f"{current_pokemon.entry} removed")
                return current_pokemon
            
    def search(self, key):
        self._rec_search(self.root, key)

    def _rec_search(self, cur, key):
        if cur != None:
            if key < cur.entry:
                if cur.left != None:
                    self._rec_search(cur.left, key)

            elif key > cur.entry:
                if cur.right != None:
                    self._rec_search(cur.right, key)

            elif cur.entry == key:
                print("Pokemon found:\n"
                f"{cur.entry}")
                return
        else:
            return
