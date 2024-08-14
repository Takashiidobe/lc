# @leet start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        This problem asks us to return the maximum subarray product of an array.
        This requires us to keep track of the minimum result and the maximum
        result we've seen so far, since any number is present in the array.

        There are three cases:
        1. A positive number is strictly beneficial.
        2. A negative number could be beneficial or not.
        3. A zero always resets your progress.

        So, we can encode these three cases in keeping track of the min and
        max so far. Either number has 3 parts:

        1. We want to use curr, cause if the minimum and maximum are very small,
        it's better to just restart.
        2. Max * curr, because multiplying max by a large negative number or a large
        positive number can create either a large positive or small negative number.
        3. Min * curr, for the same reason.

        At the end we return the max_so_far product we've seen.
        """
        if not nums:
            return 0

        result, max_so_far, min_so_far = nums[0], nums[0], nums[0]

        for curr in nums[1:]:
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


# @leet end


def test():
    assert 2 + 2 == 4
