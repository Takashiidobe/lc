# @leet start
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        To find the redundant connection, we can use Union-Find.
        Union-Find creates groups of nodes where any node can reach any other
        node in the group. If the nodes in an edge already belong to a group,
        it's a redundant connection, because we can remove said edge and
        still reach every other node.

        So, `find` is set up as normal, where it recursively tries to find
        the parent of the provided node, `x`, and returns when it finds it.

        `union` joins two groups together. It finds the parents of both nodes,
        and if their parents are the same, they're already in the same group, so it
        does nothing. If not, it sets one of the nodes to be parent of the other.

        We can use this property of `union` and exploit it -- if two nodes
        are in the same group, the edge connecting them is redundant, so we
        can return that edge.

        For union, if the nodes have the same parent, we return True, and
        otherwise, return False. We can then detect a redundant connection in
        a graph.

        The final thing to do is to traverse the whole graph and return the answer.
        """
        n = len(edges)
        parents = {i: i for i in range(n + 1)}

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            par_x, par_y = find(x), find(y)
            if par_x != par_y:
                parents[par_x] = par_y
            return par_x != par_y

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        # unreachable due to the problem statement
        return [-1, -1]


# @leet end


def test():
    assert 2 + 2 == 4
