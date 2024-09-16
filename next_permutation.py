# @leet start
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        This question asks us to transform the input into its "next permutation",
        which is the lexicographically larger permutation of its integer.
        If that's not possible (i.e. all the numbers are strictly decreasing)
        return the original permutation (the one in increasing order).

        We can do this by looping through the list of numbers twice:
        First, we want to identify the location where the numbers stop decreasing
        when iterating from the start.

        Secondly, after we find that number, we want to find a number to swap
        with. To do so, we iterate from right to left again and try to find
        the first number that is larger than the number we found in our first
        loop.

        Afterwards, we swap those numbers, and then reverse the numbers up to
        our first location, in order to generate the smallest nexct permutation.
        """
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# @leet end


def test():
    assert 2 + 2 == 4
