class Node:
    def __init__(self):
        """Create an empty tree."""
        self.key = None
        self.left = None
        self.right = None

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        if key == self.key:
            return
        if key < self.key:
            if not self.left:
                self.left = self.__class__()
            target = self.left
        else:
            if not self.right:
                self.right = self.__class__()
            target = self.right
        target.insert(key)

tree = Node()
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)

print(tree.key)
print(tree.left.key)
    

    