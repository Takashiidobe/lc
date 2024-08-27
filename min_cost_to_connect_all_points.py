from heapq import heappop, heappush


# @leet start
def manhattan_distance(p1: list[int], p2: list[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        This question asks us the minimum cost to connect all points
        in a given graph, with the distasnce being the manhattan distance.
        So, this is a Minimum Spanning Tree (MST) problem.

        We can use Prim's algorithm for this, which uses a heap to greedily
        find the lowest-weighted edge that connects a node outside of the MST
        to one that's in the MST.
        As well, since an MST can only have $n - 1$ edges, once we've iterated
        that many times, we can break out of the loop.

        So the algorithm is as follows:
        1. Create a min-heap with the starting node, 0, and a cost of 0.
        2. For each point, we want to find the minimum
        distance that this point has to connect to all the other points
        if we choose this current point.
        2a. If we've already visited this point's neighbors, ignore it.
        2b. If the total distance to this node's neighbors is larger than
        the current distance, ignore it.
        2c. Otherwise, we've found a new shortest path to the node. We update
        our distance and check if any shorter distances exist.

        Finally, after $n$ iterations, we exit. This algorithm takes $O(n^2) * log\{n}$ time
        and O(n^2)$ space.
        """
        n = len(points)
        visited = set()
        heap_dict = {0: 0}
        min_heap = [(0, 0)]

        mst_weight = 0

        while min_heap:
            w, u = heappop(min_heap)

            if u in visited or heap_dict.get(u, float("inf")) < w:
                continue

            visited.add(u)
            mst_weight += w

            for v in range(n):
                if v not in visited:
                    new_distance = manhattan_distance(points[u], points[v])

                    if new_distance < heap_dict.get(v, float("inf")):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))

        return mst_weight
