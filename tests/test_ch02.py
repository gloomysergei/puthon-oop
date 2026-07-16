from py_files.ch02 import Node


def test_node():
    tree = Node(
        9,
        Node(
            4,
            Node(8),
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
    assert len(tree) == 9
    assert tree.total() == 96
    assert tree.to_list() == [9, 4, 8, 6, 3, 7, 17, 22, 20]
    assert tree.every(lambda key: key <= 22) is True
    assert tree.every(lambda key: key < 22) is False
    assert tree.some(lambda key: key == 22) is True
    assert tree.some(lambda key: key > 22) is False
    assert tree.minimum() == 3
    assert tree.maximum() == 22


class N(Node):
    """A simple subclass of Node."""


def test_node_repr():
    tree = Node(3, Node(1), Node(2))
    assert repr(tree) == "Node(3, Node(1, None, None), Node(2, None, None))"

    tree_of_n = N(3, N(1), N(2))
    assert repr(tree_of_n) == "N(3, N(1, None, None), N(2, None, None))"