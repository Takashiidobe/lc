# @leet start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        This question asks us to find the subarray with the maximum bitwise AND
        and return its length.

        To find the maximum bitwise AND, we know we have at least one (the max
        number in the array). Then, we know that Bitwise ANDing successive numbers
        only decreases or keeps the number the same. So we just want to count
        the longest length of the max number.
        """
        max_val, ans, curr = max(nums), 0, 0

        for num in nums:
            if num == max_val:
                curr += 1
            else:
                curr = 0
            ans = max(ans, curr)
        return ans


# @leet end


def test():
    assert 2 + 2 == 4
