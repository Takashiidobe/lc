from typing import Optional


# @leet start
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        This problem asks us to clone a graph. To do so, we want to dfs
        through the provided node and return an exact copy.

        The graph can contain cycles, so we need to have a visited dictionary
        to break those cycles. The dictionary can contain a copy of the node
        it's copying, and return that when needed.

        And then for each neighbor we dfs through and add that to our
        current node's neighbors.
        """
        visited = {}

        def dfs(node):
            if node is None:
                return None
            if node in visited:
                return visited[node]
            copy = Node(node.val, [])
            visited[node] = copy
            copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return copy

        return dfs(node)


# @leet end


def test():
    assert 2 + 2 == 4
