# 200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

%

This problem wants us to count the number of islands, where a 1 indicates
land, and 0 is water, and an island is either surrounded by water
or, if it touches an edge, that is also water.

To do this, we can iterate through the grid, and when we find an island
we continue to check 4-dimensionally around it, marking other 1s we see
as part of the same island.
Finally, we return that count at the end.


```python
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        count = 0

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not inbounds(y, x) or (y, x) in visited or grid[y][x] == '0':
                return
            visited.add((y, x))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dy, dx in dirs:
                new_y, new_x = dy + y, dx + x
                dfs(new_y, new_x)

        for y in range(m):
            for x in range(n):
                if (y, x) not in visited and grid[y][x] == '1':
                    dfs(y, x)
                    count += 1
        return count


```
