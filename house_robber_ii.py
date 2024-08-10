from functools import cache


# @leet start
class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        This question is like house robber, but you're robbing a circular
        array instead of a line.

        This is the same as house robber 1, but you can pass in a boolean that
        allows you to see if you've robbed the house before.
        """

        @cache
        def dp(i, robbed):
            if i >= len(nums) or (i == len(nums) - 1 and robbed):
                return 0
            rob_curr = nums[i] + dp(i + 2, robbed if i != 0 else True)
            rob_next = dp(i + 1, robbed)
            return max(rob_curr, rob_next)

        return dp(0, False)


def test():
    assert 2 + 2 == 4
