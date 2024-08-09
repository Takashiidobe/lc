from functools import lru_cache


# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This question is just fibonacci.
        """

        @lru_cache
        def recurse(n):
            if n < 2:
                return 1
            return recurse(n - 1) + recurse(n - 2)

        return recurse(n)


# @leet end


def test():
    assert 2 + 2 == 4
