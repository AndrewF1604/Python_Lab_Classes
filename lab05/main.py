import timeit

from functools import lru_cache
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add_child(self, parent, child_value):
        new_child = TreeNode(child_value)
        parent.children.append(new_child)

    @property
    def min_value(self):
        return self._find_min_value(self.root)

    def _find_min_value(self, node):
        if not node.children:
            return node.value

        min_value = node.value
        for child in node.children:
            min_value = min(min_value, self._find_min_value(child))

        return min_value

tree = Tree(10)
tree.add_child(tree.root, 5)
tree.add_child(tree.root, 15)
tree.add_child(tree.root.children[0], 3)
tree.add_child(tree.root.children[0], 7)

print(f"MIN:{tree.min_value}")

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


czas_rekurencyjnie = timeit.timeit("fib(20)", globals=globals(), number=1000)
print(f"Fibonacci: {czas_rekurencyjnie} sekundy")

@lru_cache(maxsize=None)
def fib_lru_cache(n):
    if n <= 1:
        return n
    else:
        return fib_lru_cache(n-1) + fib_lru_cache(n-2)

czas_z_lru_cache = timeit.timeit("fib_lru_cache(20)", globals=globals(), number=1000)
print(rf"@lru_cache: {czas_z_lru_cache} sekundy")






