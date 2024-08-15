from collections import defaultdict
from heapq import heappush, heappop


# @leet start
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        This question asks us to find the shortest path to all nodes starting
        from a given node, `k`.
        If we cannot reach all nodes, the count of which is `n`, return -1.

        This is a classic use for Dijkstra's algorithm. We first turn the graph
        into a key value mapping of source -> (cost, target).

        We do this because we want to create a min heap, required for dijkstra's.
        We then create a heap, which starts out with our starting node, `k`.

        Next, we pop from the heap and check if we've visited the node already.
        If so, we continue, otherwise, we know we have the minimum cost
        to get to the node. Then, for all of its neighbors, we add it to the heap
        with its cost + our current cost.

        Finally, after traversing through all the nodes we can, if we can't
        reach all nodes, return -1, otherwise the maximum delay time is the
        maximum time we've encountered so far.
        """
        graph = defaultdict(list)

        for source, target, cost in times:
            graph[source].append((cost, target))

        heap = [(0, k)]
        costs = {}

        while heap:
            cost, node = heappop(heap)

            if node in costs:
                continue

            costs[node] = cost
            for neighbor_cost, neighbor in graph[node]:
                heappush(heap, (cost + neighbor_cost, neighbor))

        if len(costs) != n:
            return -1

        return max(costs.values())


# @leet end


def test():
    assert 2 + 2 == 4
