from collections import defaultdict


# @leet start
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        This problem asks us to count the connected components in an undirected
        graph. To do this, we first turn the representation into one that allows
        for fast access to a node's neighbors, a hashmap of node -> list[node].

        Afterwards, we iterate through the nodes (given as n) and then dfs through.
        We return 0 if the node was already visited, or 1 if not and visit all
        of its neighbors, taking care to add the node to visited if it wasn't
        already there to avoid cycles.

        We then return the sum of the nodes.
        """
        graph = defaultdict(list)
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        return sum(dfs(i) for i in range(n))


# @leet end


def test():
    assert 2 + 2 == 4
