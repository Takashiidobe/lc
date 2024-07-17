# @leet start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        This question gives a set of numbers from [0..n] where one number is missing.
        We could figure out the missing number by putting all items in a set,
        and iterating from [0..n] to find the missing number. This is $O(n)$ time
        and space.

        We can do better by exploiting the fact that the sum of [0..n] can be calculated
        with the formula $n * (n - 1) / 2$.

        Thus, this takes no extra time.
        """
        n = len(nums) + 1
        total = n * (n - 1) // 2
        return total - sum(nums)


# @leet end
sol = Solution()


def test():
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
