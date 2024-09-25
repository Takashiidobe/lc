# @leet start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        This question asks us to find the longest sequence of consecutive 1s
        if you're allowed to flip at most `k` 0s.
        The way we can solve this is by using a sliding window -- we open up a
        window, and then count the number of zeroes in the window, disregarding
        ones.
        If we hit more zeroes in our window than k, we keep incrementing our left
        pointer until there are less than k zeroes.
        At the end of each loop, we count the max of `i - j + 1` and return
        the max of that at the end.
        """
        zero_count, max_so_far, j = 0, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                while zero_count > k:
                    if nums[j] == 0:
                        zero_count -= 1
                    j += 1
            max_so_far = max(max_so_far, i - j + 1)
        return max_so_far


# @leet end


def test():
    assert 2 + 2 == 4
