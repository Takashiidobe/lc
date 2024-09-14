from collections import deque


# @leet start
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        This question asks us to find the shortest path that goes from the top
        left to the bottom right in a path of all zeroes.

        Since we're finding the shortest path, we should BFS this.
        So we define all the eight directions (since we can go in eight directions)
        and also define a visited set so we don't revisit the same square twice.
        We then check to make sure that we're at the last square, if we are, we
        return the amount of squares we've visited so far.
        """
        m, n = len(grid), len(grid[0])
        dirs = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        q = deque([(0, 0, 1)])
        visited = set()

        while q:
            y, x, path_len = q.popleft()
            if (y, x) in visited or not inbounds(y, x) or grid[y][x] != 0:
                continue
            visited.add((y, x))

            if y == m - 1 and x == n - 1:
                return path_len
            for dy, dx in dirs:
                new_y, new_x = dy + y, dx + x
                q.append((new_y, new_x, path_len + 1))

        return -1


# @leet end


def test():
    assert 2 + 2 == 4
