# @leet start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        To find the maximum subarray, we start off by counting the first
        number as the current and max.

        Then for all the other numbers, we only want to keep it if we added it to
        our current total and keep it only if the total is non-negative.
        We use `curr = max(curr, num + curr)` to do that for us.
        Finally, we update the max every iteration with the curr.

        At the end, we return the max we've seen so far.
        """
        curr, max_so_far = nums[0], nums[0]

        for num in nums[1:]:
            curr = max(curr, num + curr)
            max_so_far = max(max_so_far, curr)

        return max_so_far


# @leet end


def test():
    assert 2 + 2 == 4
