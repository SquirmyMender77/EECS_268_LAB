from node import Node

class BST:
    def __init__(self):
        BST.instance_created = True
        self.root = None
        self.current_A_name = None
        self.copy_file = []
        self.current_ID = None
        self.current_J_name = None
        

    def add(self, entry):
        new_pokemon = Node(entry)
        if self.root is None:
            self.root = new_pokemon
        else:
            self._add_recursive(self.root, new_pokemon)

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

    def _add_recursive(self, current_pokemon, new_pokemon):
        if new_pokemon.entry < current_pokemon.entry:
            if current_pokemon.left is None:
                current_pokemon.left = new_pokemon
                
            else:
                self._add_recursive(current_pokemon.left, new_pokemon)

        if new_pokemon.entry > current_pokemon.entry:
            if current_pokemon.right is None:
                current_pokemon.right = new_pokemon

            else:
                self._add_recursive(current_pokemon.right, new_pokemon)

        if new_pokemon.entry == current_pokemon.entry:
            raise ValueError("Duplicate pokemon will not be added to the tree.")
        

    def visit_option(self, option):
        if option == "pre" or option == "pre-order" or option == "preorder":
            self._pre_order_recursive(self.root)

        if option == "in" or option == "in-order" or option == "inorder":
            self._in_order_recursive(self.root)

        if option == "post" or option == "post-order" or option == "postorder":
            self._post_order_recursive(self.root)

    def remove(self, removed):
        l = 1

    def search(self, searched):
        l=1
