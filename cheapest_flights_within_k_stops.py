from collections import defaultdict
from heapq import heappush, heappop


# @leet start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """
        This is a Dijkstra's algorithm problem.
        We start off with some starting node, src, and put that into our
        heap with having 0 cost, 0 stops, and the id of the flight.

        Then, for each node in the heap, we pop from the top the minimum
        cost node, and check if we've made it to the destination in less
        stops than allowed.

        Otherwise, if we haven't visited this current node, or if we've
        gotten to the node in fewer stops, we say we've visited this node
        with a minimum cost of curr_stops, and then we push each of the neighbors
        of the current node to the heap.

        If we've gone through the entire heap and cannot make it at any cost
        we return -1.
        The time complexity is $O(n + E * K * log(E * K)$
        The space complexity is $O(N + E * K)$
        """
        visited = {}
        adj = defaultdict(list)

        for start, dest, price in flights:
            adj[start].append((price, dest))

        heap = [(0, 0, src)]
        while heap:
            cost, stops, node = heappop(heap)
            if node == dst and stops <= k + 1:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for price, neighbor in adj[node]:
                    heappush(heap, (cost + price, stops + 1, neighbor))
        return -1


# @leet end


def test():
    assert 2 + 2 == 4
