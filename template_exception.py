## from oop_testing.op1 import Node


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

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
        
         
    def pre_order(self, result = None):
        if result is None:
            result = []
        if self.key is not None:
            result.append(self.key)
        if self.left:
            self.left.pre_order(result)
        if self.right:
            self.right.pre_order(result)
        return result
                    
tree = Node(
    9,
    Node(
        4,
        Node(2),
        Node(
            6,
            Node(3),
            Node(7),
        ),
    ),
    Node(
        17,
        right=Node(
            22,
            Node(20),
        ),
    ),
)

result = tree.pre_order()
print(result)