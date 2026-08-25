class TreeBuilder(object):
    """Сборщик деревьев, работающий в виде менеждера контекста."""

    # BEGIN
    def __init__(self):
        """Инициализирует экземпляр сборщика."""
        self._stack = ([],)

    def __enter__(self):
        """Создаёт новый контекст."""
        self._stack = ([], self._stack)
        return self

    def __exit__(self, exception, *args):
        """Осуществляет выход из текущего контекста."""
        if exception is None:
            head, tail = self._stack
            if head:
                tail[0].append(head)
            self._stack = tail
    # END

    def add(self, value):
        """Добавляет в значение в текущую позицию в дереве."""
        # BEGIN
        self._stack[0].append(value)
        # END

    @property
    def structure(self):
        """
        Возвращает текущую структуру дерева в виде вложенных списков.

        Returns:
            Список списков вида [1, [2, 3, [4], 5], 6, [7, 8]]

        """
        # BEGIN
        return self._stack[0]
        # END