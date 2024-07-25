from collections import deque


# @leet start
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        This question asks us to count the amount of time it takes for all
        oranges in a grid to be rotten, where every fresh orange turns rotten
        if it's next a rotten orange (4-directionally) every minute.

        The way we do this is we first put all of the rotten oranges onto a queue
        and then have them rot their neighbors. If they can rot any neighbors,
        add those neighbors to the queue and decrement the count of fresh oranges.

        For each orange, we also enqueue its timestamp, which increments every
        round. This means we can go round by round without having to re-enqueue
        any old oranges or having to recopy the queue.

        If we cannot rot any more oranges (there are no more rotten oranges in
        the queue) then we return the max time if there are no fresh oranges left,
        otherwise we cannot rot all the fresh oranges and return -1.
        """
        FRESH, ROTTEN = 1, 2
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        for y in range(m):
            for x in range(n):
                if grid[y][x] == FRESH:
                    fresh_oranges += 1
                elif grid[y][x] == ROTTEN:
                    q.append((y, x, 0))

        max_time = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            y, x, time = q.popleft()
            for dy, dx in dirs:
                new_y, new_x = dy + y, dx + x
                if inbounds(new_y, new_x) and grid[new_y][new_x] == FRESH:
                    grid[new_y][new_x] = ROTTEN
                    fresh_oranges -= 1
                    q.append((new_y, new_x, time + 1))
                    max_time = max(max_time, time + 1)

        return max_time if not fresh_oranges else -1


# @leet end


def test():
    assert 2 + 2 == 4
