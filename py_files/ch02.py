import operator

class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

# BEGIN (write your solution here)

    def __len__(self):
        count = 1
        if self.left is not None:
            count += len(self.left)
            
        if self.right is not None:
            count += len(self.right)
            
        return count
    
    def __repr__(self):
        # Формируем части для left и right
        left_repr = repr(self.left) if self.left is not None else 'None'
        right_repr = repr(self.right) if self.right is not None else 'None'
        
        return f'Node({self.key!r}, {left_repr}, {right_repr})'
    
    def total():
        pass
    
    def minimum():
        pass
    
    def maximum():
        pass
    
    def to_list():
        pass
    
    def every(fn):
        pass
    
    def some(fn):
        pass
    
# END