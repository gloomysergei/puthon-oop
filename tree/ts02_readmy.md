# Задача №2

Для преобразования исходного массива в дерево используйте функцию `sorted_array_to_BST()`

```python
import solution from solution

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

solution(items)
# [
#     [5, 3, 2, 1],
#     [5, 3, 4],
#     [5, 8, 7, 6],
#     [5, 8, 9],
# ]
```

Импортируйте функцию `sorted_array_to_BST()`, чтобы использовать ее в своем решении. Для этого добавьте в файл `solution` такой код:

```python
import os
import sys

sys.path.append(os.path.abspath('/usr/src/app/'))

from helpers.helpers import sorted_array_to_BST
```
