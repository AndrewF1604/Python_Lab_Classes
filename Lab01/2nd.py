import unittest


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child_node, edge_value=None):
        self.children.append((child_node, edge_value))

    def traverse(self, result=None):
        if result is None:
            result = []
        result.append(self.value)
        for child, _ in self.children:
            child.traverse(result)
        return result

    def __str__(self):
        return str(self.value)


class TestTreeNode(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        self.child1 = TreeNode(2)
        self.child2 = TreeNode(3)
        self.child3 = TreeNode(4)

        self.root.add_child(self.child1, 'A')
        self.root.add_child(self.child2, 'B')
        self.child1.add_child(self.child3, 'C')

    def test_add_child(self):
        self.assertEqual(len(self.root.children), 2)
        self.assertEqual(len(self.child1.children), 1)

    def test_traverse(self):
        expected_result = [1, 2, 4, 3]
        self.assertEqual(self.root.traverse(), expected_result)

    def test_str(self):
        self.assertEqual(str(self.root), "1")
        self.assertEqual(str(self.child1), "2")
        self.assertEqual(str(self.child2), "3")
        self.assertEqual(str(self.child3), "4")


if __name__ == "__main__":
    unittest.main()