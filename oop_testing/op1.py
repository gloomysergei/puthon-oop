class Node:
    def __init__(self):
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