from collections import defaultdict


# @leet start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        This question asks us to find the unique paths to the bottom right square
        if we can only go down or right.

        The intuition here is that since we can only go down or right, any tile
        where we are on the first row or first col only has one way to get there
        (always right or always down). Thus, we can create a DP array, where
        the first row and first col are always 1, and then for every other square
        we know that we can get to the square in the sum of the ways of the
        square above and the square before the current square.

        Finally, we return the count of paths of the square we want, which is
        `dp[m-1][n-1]`.

        I did this using a defaultdict since it requires less setup than a DP array.
        """
        dp = defaultdict(lambda: 1)

        for i in range(1, m):
            for j in range(1, n):
                dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]

        return dp[(m - 1, n - 1)]


# @leet end


def test():
    assert 2 + 2 == 4
