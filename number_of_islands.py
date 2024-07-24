# @leet start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        This problem wants us to count the number of islands, where a 1 indicates
        land, and 0 is water, and an island is either surrounded by water
        or, if it touches an edge, that is also water.

        To do this, we can iterate through the grid, and when we find an island
        we continue to check 4-dimensionally around it, marking other 1s we see
        as part of the same island.
        Finally, we return that count at the end.
        """
        visited = set()
        m, n = len(grid), len(grid[0])
        count = 0

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not inbounds(y, x) or (y, x) in visited or grid[y][x] == "0":
                return
            visited.add((y, x))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dy, dx in dirs:
                new_y, new_x = dy + y, dx + x
                dfs(new_y, new_x)

        for y in range(m):
            for x in range(n):
                if (y, x) not in visited and grid[y][x] == "1":
                    dfs(y, x)
                    count += 1
        return count


# @leet end


def test():
    assert 2 + 2 == 4
