from collections import deque


# @leet start
class Solution:
    def pacificAtlantic(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        This question asks us to find the tiles which can reach both the pacific
        and atlantic ocean, where the pacific is the left and top edge and
        the atlantic is the bottom and right edge. Water flows from tiles if it has
        at least the same height or is greater.

        To do this, we can first create two queues, one for the pacific and atlantic
        oceans, and then add in the reachable edges for both.

        Next, we BFS from both queues. We first create a set that holds the reachable
        items, and then for each queue, we check to see if we can reach any new nodes
        by checking its neighbors and making sure its inbounds, reachable, and
        the the new value is smaller than our current x and y coordinates.
        If this is correct, we append it to the queue.

        We do this BFS for both the pacific and atlantic oceans and then do
        set intersection on them to return the set where both oceans
        are reachable.
        """
        m, n = len(matrix), len(matrix[0])

        if not matrix or not matrix[0]:
            return []

        pacific = deque()
        atlantic = deque()

        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))
        for i in range(n):
            pacific.append((0, i))
            atlantic.append((m - 1, i))

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def bfs(q):
            reachable = set()
            while q:
                y, x = q.popleft()
                reachable.add((y, x))
                for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_y, new_x = dy + y, dx + x
                    if not inbounds(new_y, new_x):
                        continue
                    if (new_y, new_x) in reachable:
                        continue
                    if matrix[new_y][new_x] < matrix[y][x]:
                        continue
                    q.append((new_y, new_x))
            return reachable

        return list(bfs(pacific) & bfs(atlantic))


# @leet end


def test():
    assert 2 + 2 == 4
