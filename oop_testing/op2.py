import operator


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# BEGIN (write your solution here)
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
    
    def __len__(self):
        return len(self.pre_order())
    
    def __repr__(self):
        if self.key is None and self.left is None and self.right is None:
            return 'None'
        return f'{self.__class__.__name__}({self.key}, {self.left!r}, {self.right!r})'
    
    def total(self):
        return sum(self.pre_order())
    
    def minimum(self):
        return min(self.pre_order())
        
    def maximum(self):
        return max(self.pre_order())
    
    def to_list(self):
        return self.pre_order()
    
    def every(self, predicate):
        def check(node):
            if node is None:
                return True
            if not predicate(node.key):
                return False
            return check(node.left) and check(node.right)
        return check(self)
    
    def some(self, predicate):
        def check(node):
            if node is None:
                return False
            if predicate(node.key):
                return True
            return check(node.left) or check(node.right)
        return check(self)
        
# END

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

result = tree.total()
print(result)