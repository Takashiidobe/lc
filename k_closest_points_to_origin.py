from heapq import heapify, heappop


# @leet start
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[tuple[int]]:
        """
        The best solution involves sorting via quickselect in $O(n)$ time.
        This solultion works in $O(n{}\log{}k)$ time and uses a min-heap.
        The heap pops off points by closest distance and saves them a list,
        and returns the list.
        """
        distances = [(x**2 + y**2, (x, y)) for x, y in points]
        heapify(distances)
        return [heappop(distances)[1] for _ in range(k)]


# @leet end
sol = Solution()


def test():
    assert sol.kClosest([[1, 3], [-2, 2]], 1) == [(-2, -2)]
    assert sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [(3, 3), (-2, 4)]
