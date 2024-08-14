from functools import cache


# @leet start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        This question asks if we can partition the list `nums` into two subsets
        where the sums are equal.

        To solve this, we note that the subset sum can only be split into two if
        it is even (odd numbers are not divisible by 2), and instead of checking
        for both the left and right subsets equaling each other, we can just check
        if one side is equal to half the subset sum (by definition, that means
        both are equal).

        We then go through each index either choosing to add the number to our
        sum or not. At any time, if our current equals the subset sum, we return
        true, or if we hit the end of the array or curr > subset sum, we return
        false.
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2

        n = len(nums)

        @cache
        def dfs(i, curr):
            if curr == subset_sum:
                return True
            if curr > subset_sum or i == n:
                return False
            return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

        return dfs(0, 0)


# @leet end


def test():
    assert 2 + 2 == 4
