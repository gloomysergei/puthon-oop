from oop_testing.op3 import TreeBuilder


def test_tree_builder():
    tree = TreeBuilder()
    tree.add('root')
    with tree:
        tree.add('first child')
        tree.add('second child')
        with tree:
            tree.add('grandchild')
        tree.add('bastard')
        with tree:  # this subtree is empty intentionally
            pass    # we need to do nothing
        tree.add('another bastard')

    assert tree.structure == [
        'root',
        [
            'first child',
            'second child',
            ['grandchild'],
            'bastard',
            'another bastard',
        ],
    ]
