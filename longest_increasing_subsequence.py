# @leet start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        For this problem we're tasked with returning the length of the longest increasing
        subsequence. For
        [10, 9, 2, 5, 3, 7, 101, 18], that would be [2, 3, 7, 101]

        If we do this naively, this can be done with DFS in (2^n) time, because
        for every number, we want to find the numbers that are larger than it
        recursively, which requires n * n computations for n items.

        To make this faster, we have to solve subproblems for each number.

        For each number, we know the value of the numbers previous to it.
        We also can store the longest increasing subsequence up to that point
        in an extra array. Thus, we can solve this problem by building up
        the longest increasing subsequence by iterating through the array
        and for every item, building up a recurrence relation, where $v_i$ is
        the max of all the items that came before it + 1 if it is smaller
        than the number, otherwise, just the number itself.

        We can do this for all the items in the given array and return the max
        of our answers, which answers the question.
        """
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# @leet end


def test():
    assert 2 + 2 == 4
