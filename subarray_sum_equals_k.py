from collections import defaultdict


# @leet start
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Given an array and an integer, k, return the number of subarrays that
        have a sum of k.

        To find this out, we can find the total sum up to this point, i.
        If we find the same i, we know that the sum of indexes between
        the two points is 0. Thus, we've found another subarray that adds
        to k, and we need to increment the count of subarrays equal k by
        the amount of times we've seen the same `number - k`.
        """
        count, total = 0, 0
        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            total += num
            count += sums[total - k]
            sums[total] += 1
        return count


# @leet end


def test():
    assert 2 + 2 == 4
