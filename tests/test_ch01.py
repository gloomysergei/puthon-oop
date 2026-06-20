from py_files.ch01 import Node


def test_empty_node():
    tree = Node()
    assert tree.key is None
    assert tree.left is None
    assert tree.right is None


def test_node():
    tree = Node()
    tree.insert(9)
    tree.insert(17)
    tree.insert(4)
    tree.insert(3)
    tree.insert(6)
    tree.insert(22)
    tree.insert(5)
    tree.insert(7)
    tree.insert(20)
    tree.insert(4)
    tree.insert(3)

    assert tree.key == 9

    assert tree.left.key == 4

    assert tree.left.left.key == 3
    assert tree.left.left.left is None
    assert tree.left.left.right is None

    assert tree.left.right.key == 6

    assert tree.left.right.left.key == 5
    assert tree.left.right.left.left is None
    assert tree.left.right.left.right is None

    assert tree.left.right.right.key == 7
    assert tree.left.right.right.left is None
    assert tree.left.right.right.right is None

    assert tree.right.key == 17
    assert tree.right.left is None

    assert tree.right.right.key == 22
    assert tree.right.right.right is None

    assert tree.right.right.left.key == 20
    assert tree.right.right.left.left is None
    assert tree.right.right.left.right is None


class NewNode(Node):
    """A simple subclass of Node."""


def test_liskov_substitution():

    tree = NewNode()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    assert isinstance(tree.left, NewNode), "Sibling should be NewNode too"
    assert isinstance(tree.right, NewNode), "Sibling should be NewNode too"
