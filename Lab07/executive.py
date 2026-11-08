from BST import BST

class Executive:
    def __init__(self):
        self.bst = BST()

    def add_values(self, values):
        for value in values:
            self.bst.add(int(value))