### Полный код метода

```python
def delete(self, value):
    """Удаляет узел с заданным значением из дерева."""
    # Ищем узел для удаления и его родителя
    node_to_delete, parent, found = self.__find(self.root, None, value)
    
    if not found:
        return False  # Элемент не найден, удалять нечего
    
    # Случай 1: узел — лист (нет потомков)
    if node_to_delete.left is None and node_to_delete.right is None:
        self._delete_leaf(node_to_delete, parent)
    
    # Случай 2: узел имеет одного потомка
    elif node_to_delete.left is None or node_to_delete.right is None:
        self._delete_node_with_one_child(node_to_delete, parent)
    
    # Случай 3: узел имеет двух потомков
    else:
        self._delete_node_with_two_children(node_to_delete)
    
    return True
```

### Вспомогательные методы

1. Удаление листа `_delete_leaf`

```python
def _delete_leaf(self, node, parent):
    """Удаляет лист (узел без потомков)."""
    if parent is None:  # Удаляем корень
        self.root = None
    elif parent.left == node:  # Узел — левый потомок
        parent.left = None
    else:  # Узел — правый потомок
        parent.right = None

2. Удаление узла с одним потомком `_delete_node_with_one_child`

```python
def _delete_node_with_one_child(self, node, parent):
    """Удаляет узел с одним потомком."""
    # Определяем существующего потомка
    child = node.left if node.left else node.right
    
    if parent is None:  # Удаляем корень
        self.root = child
    elif parent.left == node:  # Узел — левый потомок
        parent.left = child
    else:  # Узел — правый потомок
        parent.right = child

3. Удаление узла с двумя потомками `_delete_node_with_two_children`

```python
def _delete_node_with_two_children(self, node):
    """Удаляет узел с двумя потомками, заменяя его преемником."""
    # Находим преемника (минимальный узел в правом поддереве)
    successor = self._find_min(node.right)
    successor_parent = self._find_parent(node, successor)
    
    # Копируем значение преемника в удаляемый узел
    node.data = successor.data
    
    # Удаляем преемника (у него максимум один потомок)
    if successor_parent.left == successor:
        successor_parent.left = successor.right
    else:
        successor_parent.right = successor.right
```

### Вспомогательные методы для поиска

```python
def _find_min(self, node):
    """Находит минимальный узел в поддереве (самый левый)."""
    while node.left:
        node = node.left
    return node

def _find_parent(self, start_node, target_node):
    """Находит родителя заданного узла."""
    if start_node == target_node:
        return None
    
    current = start_node
    parent = None
    while current:
        if current.data == target_node.data:
            return parent
        parent = current
        if target_node.data < current.data:
            current = current.left
        else:
            current = current.right
    return None
```

### Подробное объяснение логики

Три случая удаления:

1. Узел — лист (нет потомков)

    - Просто удаляем ссылку на узел у его родителя.
    - Если удаляем корень — устанавливаем `self.root = None`.

2. Узел имеет одного потомка

    - «Обходим» удаляемый узел: родитель ссылается напрямую на потомка.
    - Потомка подвешиваем к родителю вместо удаляемого узла.

3. Узел имеет двух потомков

    - Находим преемника — минимальный узел в правом поддереве (он больше всех в левом и меньше всех в правом)
    - Копируем значение преемника в удаляемый узел.
    - Удаляем преемник (у него всегда максимум один потомок — правый).

### Примеры работы

#### Пример 1. Удаление листа

Дерево:

    10
   /  \
  5    15
      /
     12

*Удаляем 12*:

- 12 — лист;
- родитель 15 теряет ссылку на 12;
- дерево остаётся корректным.

#### Пример 2. Удаление узла с одним потомком

Дерево:

    10
   /  \
  5    15
        \
         20

*Удаляем 15:*

- у 15 есть один потомок 20;
- 10.right теперь ссылается на 20 вместо 15;
- 20 становится прямым потомком 10.

#### Пример 3. Удаление узла с двумя потомками

Дерево:

    10
   /  \
  5    15
      /  \
     12   20

*Удаляем 15:*

- находим преемника: минимальный в правом поддереве — 12;
- копируем 12 в узел 15 (теперь узел 15 содержит 12);
- удаляем исходный узел 12 (он лист);
- итоговое дерево:

    10
   /  \
  5    12
        \
         20
         