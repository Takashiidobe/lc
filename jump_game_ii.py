from functools import cache


# @leet start
class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        This question asks us to find the shortest path from index 0 to the last
        index, given an array counting the number of steps we can jump up to.

        We can do this by breaking this problem down into its subsequent cases:
        1. if we ask for an index to the right of the array, we've cleared it,
        so we return 0.
        2. If our current number is 0, we return infinity because we can't reach
        the end from here.
        3. Otherwise, we check all of our next positions, which is the range
        1..nums[i], and return 1 + the minimum of that.

        Finally, we start at the first index and return the number of steps taken.
        """
        n = len(nums)

        @cache
        def dp(i):
            if i >= n - 1:
                return 0
            elif nums[i] == 0:
                return float("inf")
            else:
                return 1 + min(dp(i + x) for x in range(1, nums[i] + 1))

        return dp(0)


# @leet end


def test():
    assert 2 + 2 == 4
