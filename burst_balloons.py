from functools import cache


# @leet start
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        We want to be able to get the maximum coins by bursting balloons.
        This is a 2D DP problem.

        First, we can handle edge cases by adding the 1s to the end of our
        current nums.

        Next, we define the dp function, which returns the max gain for popping
        this particular window of balloons.

        The dp function iterates through all the balloons and keeps track of
        popping the ith balloon last.

        We then keep the max of this by the end.

        Finally, we call the dp function, but give the range removing the balloons
        we added in.
        """
        nums = [1] + nums + [1]

        @cache
        def dp(l, r):
            if l > r:
                return 0
            result = 0

            for i in range(l, r + 1):
                gain = nums[l - 1] * nums[i] * nums[r + 1]
                remaining = dp(l, i - 1) + dp(i + 1, r)
                result = max(result, remaining + gain)

            return result

        return dp(1, len(nums) - 2)


# @leet end


def test():
    assert 2 + 2 == 4
