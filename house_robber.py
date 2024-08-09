from functools import cache


# @leet start
class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        In this question, you are given an array of payoffs, where you can either
        take the current payoff, or skip it. The reason why you would skip it
        is because if you take the current number, you can't take the next number.

        So, we can create a dp array, where you can either choose the current
        number + 2 indexes, or you can choose to skip and just take the result
        of the next index.

        We can turn this into code, and then return the maximum of the array.
        """
        n = len(nums)

        @cache
        def dp(i):
            if 0 <= i < n:
                return max(nums[i] + dp(i + 2), dp(i + 1))
            else:
                return 0

        return max(dp(i) for i in range(n))


# @leet end


def test():
    assert 2 + 2 == 4
