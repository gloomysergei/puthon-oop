# класс для формирования узла
class Node:
    def __init__(self, data): # data - данные узла
        self.data = data
        self.left = self.right = None # указатели
# при создании объекта с использованием класса Node создается объект с листовыми вершинами 

# класс Tree для работы с деревом, вначале он создается пустым
class Tree:
    def __init__(self):
        self.root = None
      
    def __find(self, node, parent, value):
        
        if node is None: # базовый случай рекурсии. Дошли до конца ветки дерева
            return None, parent, False
        
        if value == node.data:
            return node, parent, True # флаг наличия элемента
        
        if value < node.data:   # node.date - текущее значение узла. Идем влево
            if node.left:       # если существует левый потомок, включаем рекурсию
                return self.__find(node.left, node, value)
            
        if value > node.data:   # node.date - текущее значение узла. Идем вправо
            if node.right:       # если существует правый потомок, включаем рекурсию
                return self.__find(node.right, node, value)  
            
        return node, parent, False #  не нашли вершину с соответствующим значением value
                # node - узел к которому будем добавлять значение value
                # parent - родитель узла node 
        
    def append(self, obj): # метод добавления вершин. obj - объект класса Node
        # если указатель root=None ---> Tree не содержит ни одного объекта
        # то новая вершина должна добавляться как корневая
        if self.root is None:
            self.root = obj
            return obj
        # если условие не срабатывает, то мы должны:
        # -найти вершину (получить ссылку), к которой затем добавляем новую вершину
        # - используем метод __find
        
        s, p, fl_find = self.__find(self.root, None, obj.data)
        
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
                
        return obj # возвращаем объект который добавили
    
    # метод отображающий бинарное дерево
    def show_tree(self, node):
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)
        
    # метод отображающий бинарное дерево в ширину
    def show_wide_tree(self, node):
        if node is None:
            return
        
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
                    
            print()
            v = vn
            
    # метод удаления листовой вершины
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None # удаляем ссылку на лист
        elif p.right == s:
            p.right = None
    
    # метод удаления узла  или с левым или с правым потомком      
    def __del_one_child(self, s, p):
        if p.left == s: 
            if s.left is None: # если левый потомок у удаляемой вершины отс.
                p.left = s.right # переопределение связей
            elif s.right is None: # если правый  потомок у удаляемой вершины отс.
                p.left = s.left 
        elif p.right == s: # если правый потомок у удаляемой вершины отс.
            if s.left is None: # если левый потомок у удаляемой вершины отс.
                p.right = s.right # переопределение связей
            elif s.right is None: # если правый  потомок у удаляемой вершины отс.
                p.right = s.left  
                
                       
    # метод нахождения min значения в поддереве и его родителя
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent
               
    # метод удаление узла с значением key
    def del_node(self, key):

        s, p, fl_find = self.__find(self.root, None, key)  # ищем узел с значением key
        
        if not fl_find:
            return None # узел не найден
        # 1. условие для удаления листовой вершины
        if s.left is None and s.right is None:
            
            # метод удаления листа, s-удаляемый узел, p - его родитель
            self.__del_leaf(s, p)
            
        # 2. условие для удаления вершины или с левым или с правым потомком
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
            
         # 3. условие для удаления полной вершины   
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    
v = [10, 5, 7, 16, 13, 2, 20] 

t = Tree()

for x in v:
    t.append(Node(x))
    
t.show_tree(t.root)
          
            