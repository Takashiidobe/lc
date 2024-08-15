from typing import Optional


# @leet start


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        This question asks to copy a list where the nodes have a random pointer,
        which can point to anywhere in the list.

        Given this constraint, we have to copy the list. We can treat this as if
        it was a graph, and try to clone it, where have a visited set to count
        for cycles.

        We copy each node by making a new instance of the passed in node given
        a value, and maintaining a cache with a new copy of the list.

        We then make sure to copy the random and next pointers for every value
        in the list by returning `traverse(node.random)` and `traverse(node.next)`
        before returning our copied node.
        """
        visited = {}

        def traverse(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy

            copy.random = traverse(node.random)
            copy.next = traverse(node.next)
            return copy

        return traverse(head)


# @leet end


def test():
    assert 2 + 2 == 4
