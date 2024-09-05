from functools import cache
from math import floor, sqrt


# @leet start
class Solution:
    def numSquares(self, n: int) -> int:
        """
        This question asks us to return the minimum number of squares to
        sum up to a number. This can be done with lagrange's theorem, but I
        did the DP version instead, where I test all numbers in $O(n^2)$ time that
        add up to the number and return the shortest path.
        """

        @cache
        def dp(n):
            if n <= 1:
                return n
            if n == floor(sqrt(n)) ** 2:
                return 1

            min_count = n
            for i in range(1, floor(sqrt(n)) + 1):
                min_count = min(min_count, dp(n - i * i))
            return min_count + 1

        return dp(n)


# @leet end


def test():
    assert 2 + 2 == 4
