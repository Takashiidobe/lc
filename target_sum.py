from functools import cache


# @leet start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        This question asks us to find the number of ways to assign
        addition or subtraction signs to a set of numbers num to get to a target.
        We know that we can use dfs in $O(2^n)$ to do this, since for each number,
        we can either add or subtract it from our running total.

        If we add caching to this, we can reduce the time complexity to $O(t * n)$.
        """
        n = len(nums)

        @cache
        def dfs(total, i):
            if i == n:
                return 1 if total == target else 0
            else:
                return dfs(total + nums[i], i + 1) + dfs(total - nums[i], i + 1)

        return dfs(0, 0)


# @leet end


def test():
    assert 2 + 2 == 4
