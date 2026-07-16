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
        if key < self.key: # если новый ключ меньше текущего узла, он должен быть в левом поддереве
            
            # это проверка «а есть ли уже левый ребёнок».
            # not self.left истинно, когда self.left равно None (то есть слева пусто).
            if not self.left: # если левого ребенка нет — создаём новый узел.
                self.left = self.__class__() # создается пустой узел
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
    

    