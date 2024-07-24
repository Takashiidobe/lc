# @leet start
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        This problem asks to find the area of the largest island,
        where an island is denoted by the number 1, and water is the number 0.

        To find the max area, we iterate through the grid until we find a 1.
        Then, the area of that island is 1 + the rest of the nodes dfsed.

        We need to keep a visited set so we don't visit the same islands again
        for each new island we see, make sure to update the max length with the
        max length we've seen so far.
        """
        m, n = len(grid), len(grid[0])
        max_size = 0
        visited = set()

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not inbounds(y, x) or (y, x) in visited or grid[y][x] == 0:
                return 0
            visited.add((y, x))
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            return 1 + sum(dfs(dy + y, dx + x) for dy, dx in dirs)

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    max_size = max(max_size, dfs(y, x))

        return max_size


# @leet end


def test():
    assert 2 + 2 == 4
