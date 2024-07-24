from collections import defaultdict, deque


# @leet start
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        A graph is a tree if it has n - 1 edges
        And a graph is a valid tree if you can visit every node and there's no
        simple cycles.
        """
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        q = deque([0])

        visited = {0}

        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)

        return len(visited) == n


# @leet end
q = Solution().validTree


def test():
    assert q(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    assert not q(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
