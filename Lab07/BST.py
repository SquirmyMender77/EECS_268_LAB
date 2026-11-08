from node import Node

class BST:
    def __init__(self):
        self.root = None
        self.current_node = None

    def add(self, entry):
        new_node = Node(entry)
        if self.root is None:
            self.root = new_node
            self.current_node = self.root
            print(f"{new_node.entry} added to the root")

        else:
            self._add_recursive(self.current_node, new_node)

    def _add_recursive(self, current_node, new_node):
        if new_node.entry < current_node.entry:
            if current_node.left is None:
                if new_node.entry < current_node.entry:
                    current_node.left = new_node
                    print(f"{new_node.entry} added to the left of {current_node.entry}")
                    return

                if new_node.entry > current_node.entry:
                    current_node.right = new_node
                    print(f"{new_node.entry} added to the right of {current_node.entry}")
                    return
                
            if current_node.left is not None:
                if new_node.entry < current_node.entry:
                    if current_node.left is None:
                        current_node.left = new_node
                        print(f"{new_node.entry} added to the left of {current_node.entry}")
                        return
                    
                    if current_node.left is not None:
                        self._add_recursive(current_node.left, new_node)

                if new_node.entry > current_node.entry:
                    if current_node.right is None:
                        current_node.right = new_node
                        print(f"{new_node.entry} added to the right of {current_node.entry}")
                        return
                    
                    if current_node.right is not None:
                        self._add_recursive(current_node.right, new_node)
            
        if new_node.entry > current_node.entry:
            if current_node.right is None:
                current_node.right = new_node
                print(f"{new_node.entry} added to the right of {current_node.entry}")
                return

            if current_node.right is not None:
                if new_node.entry < current_node.entry:
                    if current_node.left is None:
                        current_node.left = new_node
                        print(f"{new_node.entry} added to the left of {current_node.entry}")

                        return
                    
                    if current_node.left is not None:
                        self._add_recursive(current_node.left, new_node)

                if new_node.entry > current_node.entry:
                    if current_node.right is None:
                        current_node.right = new_node
                        print(f"{new_node.entry} added to the right of {current_node.entry}")
                        return
                    
                    if current_node.right is not None:
                        self._add_recursive(current_node.right, new_node)


        if new_node.entry == current_node.entry or new_node.entry == self.root.entry:
            print(f"{new_node.entry} is already in the tree. Duplicate value will not be added to the tree.")

    def _pre_order_recursive(self, current_node):
        if current_node is not None:
            print(current_node.entry)
            self._pre_order_recursive(current_node.left)
            self._pre_order_recursive(current_node.right)

        if self.root == None:
            print("Cannot traverse an empty tree")

    def _in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left)
            print(current_node.entry)
            self._in_order_recursive(current_node.right)

        if self.root == None:
            print("Cannot traverse an empty tree")

    def _post_order_recursive(self, current_node):
        if current_node is not None:
            self._post_order_recursive(current_node.left)
            self._post_order_recursive(current_node.right)
            print(current_node.entry)

        if self.root == None:
            print("Cannot traverse an empty tree")   

    def visit_option(self, option):
        if option == "pre" or option == "pre-order" or option == "preorder":
            self._pre_order_recursive(self.root)

        elif option == "in" or option == "in-order" or option == "inorder":
            self._in_order_recursive(self.root)

        elif option == "post" or option == "post-order" or option == "postorder":
            self._post_order_recursive(self.root)

        else:
            user_option = input("Invalid input, please enter a valid traversal method (pre, in, post): ")
            self.visit_option(user_option)