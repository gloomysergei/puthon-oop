class TreeBuilder:
    """Сборщик деревьев, работающий в виде менеджера контекста."""

    def __init__(self):
        self._root = []          # Корневая структура
        self._stack = [self._root]  # Стек: каждый элемент — текущий активный список

    def __enter__(self):
        # Создаём новый узел (пустой список)
        new_node = []
        # Добавляем в текущий (верхний в стеке)
        self._stack[-1].append(new_node)
        # Теперь этот узел становится текущим
        self._stack.append(new_node)
        return self

    def __exit__(self, exc_type, exc, tb):
        # Удаляем текущий узел из стека
        current = self._stack.pop()
        # Если он пустой — удаляем из родителя
        if not current:
            parent = self._stack[-1]
            # current — это последний элемент parent, потому что мы только что его туда добавили
            parent.pop()
        return False

    def add(self, value):
        """Добавляет значение в текущую позицию в дереве."""
        # Просто добавляем в текущий активный список (верх стека)
        self._stack[-1].append(value)

    @property
    def structure(self):
        """Возвращает текущую структуру дерева в виде вложенных списков."""
        return self._root
