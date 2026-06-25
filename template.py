class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.left = None  # ссылка на левый дочерний узел
        self.right = None  # ссылка на правый дочерний узел
        self.parent = parent  # ссылка на родителя
        self.value = value  # полезная нагрузка
        
    def find_node(self, value): # поиск узла
        node = self
        while node:
            if value == node.value:
                return node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return None