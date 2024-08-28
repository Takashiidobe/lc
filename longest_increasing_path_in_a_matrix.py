from math import inf


# @leet start
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """
        This question asks us to find the longest increasing path in a matrix
        We can do this by DFSing through the entire matrix, keeping track of
        the previous value to make sure our number is always strictly increasing,
        but this would have a time complexity of $O(2^n)$.
        We want and $O(n)$ solution, and we can get one with caching. We first
        define a cache, which holds the longest increasing path from this node.
        Then, we dfs through, checking the cache to see if we've already visited
        that node. If we have, we return that, if we go out of bounds or if
        we aren't increasing anymore, we return 0.

        Finally, we save the max we see 4-dimensionally in a variable, and
        add it to our cache before returning it, so that other recursive calls
        of the function can use our computation.
        """
        m, n = len(matrix), len(matrix[0])
        cache = {}

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x, prev):
            if not inbounds(y, x) or matrix[y][x] <= prev:
                return 0
            if (y, x) in cache:
                return cache[(y, x)]

            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            ans = 1 + max(dfs(dy + y, dx + x, matrix[y][x]) for dy, dx in dirs)
            cache[(y, x)] = ans
            return ans

        for y in range(m):
            for x in range(n):
                dfs(y, x, -inf)

        return max(cache.values())


# @leet end


def test():
    assert 2 + 2 == 4
