"""
Author: Preston Dahl 
Date: 2026-11-16
Lab: lab08
Last modified: 2026-11-16
Purpose: The internals of the operation implmented with an imporved Binary Search Tree with remove, and search.
"""

from pokeball import Pokeball

class Pokedex_internals:
    def __init__(self):
        Pokedex_internals.instance_created = True
        self.root = None
        self.current_A_name = None
        self.copy_file = []
        self.current_ID = None
        self.current_J_name = None
        self.Failed = False


    # Set the Failed check to False on every function startup
    # Whenever a Function fails, the False check is set to True and the function returns
    def add(self, pokemon):
        self.Failed = False
        new_pokemon = Pokeball(pokemon)
        if self.root is None:
            self.root = new_pokemon
        else:
            self._add_recursive(self.root, new_pokemon)

    def _add_recursive(self, current_pokemon, new_pokemon):
        if new_pokemon.entry < current_pokemon.entry:
            if current_pokemon.left is None:
                current_pokemon.left = new_pokemon
                return
                
            else:
                self._add_recursive(current_pokemon.left, new_pokemon)

        if new_pokemon.entry > current_pokemon.entry:
            if current_pokemon.right is None:
                current_pokemon.right = new_pokemon
                return

            else:
                self._add_recursive(current_pokemon.right, new_pokemon)

        if new_pokemon.entry == current_pokemon.entry:
            print(f"|{f"{new_pokemon.entry} wasn't added because {current_pokemon.entry} already exists.".center(146)}|")
            self.Failed = True
            return

    def _pre_order_recursive(self, pokemon):
        if pokemon is not None:
            print(f"|{f"{pokemon.entry}".center(146)}|")
            self._pre_order_recursive(pokemon.left)
            self._pre_order_recursive(pokemon.right)

    def _in_order_recursive(self, pokemon):
        if pokemon is not None:
            self._in_order_recursive(pokemon.left)
            print(f"|{f"{pokemon.entry}".center(146)}|")
            self._in_order_recursive(pokemon.right)

    def _post_order_recursive(self, pokemon):
        if pokemon is not None:
            self._post_order_recursive(pokemon.left)
            self._post_order_recursive(pokemon.right)
            print(f"|{f"{pokemon.entry}".center(146)}|")

    def visit_option(self, option):
        self.Failed = False
        if option == "pre" or option == "pre-order" or option == "preorder":
            self._pre_order_recursive(self.root)
 
        if option == "in" or option == "in-order" or option == "inorder":
            self._in_order_recursive(self.root)
 
        if option == "post" or option == "post-order" or option == "postorder":
            self._post_order_recursive(self.root)

    def remove(self, key):
        self.Failed = False
        # Set the root to be the parent of the Tree
        self.root = self._rec_remove(self.root, key)
        
    def _rec_remove(self, current_pokemon, key):
        if current_pokemon == None:
            self.Failed = True
            return

        if key > current_pokemon.entry:
            current_pokemon.right = self._rec_remove(current_pokemon.right, key)
            return current_pokemon

        if key < current_pokemon.entry:
            current_pokemon.left = self._rec_remove(current_pokemon.left, key)
            return current_pokemon

        if current_pokemon.entry == key:
            # Left subtree is empty and right is not so the new parent is the right subtree
            if current_pokemon.right == None and current_pokemon.left != None:
                return current_pokemon.left

            # Right subtree is empty and left is not so the new parent is the left subtree
            if current_pokemon.right != None and current_pokemon.left == None:
                return current_pokemon.right

            # Both Subtrees are empty so the parent is just none
            if current_pokemon.right == None and current_pokemon.left == None:
                return None

            # Both subtrees aren't empty so a temporary variable looking at the left is created to check for greatest value in the left subtree
            if current_pokemon.right != None and current_pokemon.left != None:
                temp = current_pokemon.left

                # Check for largesty value in left subtree by going right until None is next
                while temp.right is not None:
                    temp = temp.right
                # Once None is reached, the greatest value entry gets stored to current_pokemon and then the new parent is the greatest value
                current_pokemon.entry = temp.entry
                current_pokemon.left = self._rec_remove(current_pokemon.left, current_pokemon.entry)
                return current_pokemon

    # I just used a simple check left if it's smaller and then check right if it's bigger implemntation to find the correct entry otherwise a Failed = True
    def search(self, ID):
        self.Failed = False
        self._rec_search(self.root, ID)

    def _rec_search(self, pokemon, ID):
        if ID < pokemon.entry:
            if pokemon.left != None:
                self._rec_search(pokemon.left, ID)
                
            if pokemon.left == None and pokemon.entry != ID:
                self.Failed = True
                return

        if ID > pokemon.entry:
            if pokemon.right != None:
                self._rec_search(pokemon.right, ID)

            if pokemon.right == None and pokemon.entry != ID:
                self.Failed = True
                return

        if pokemon.entry == ID:
            print(f"|{f"Pokemon ID {ID} found:".center(146)}|")
            print(f"|{f"{pokemon.entry}".center(146)}|")
            return pokemon.entry

        
