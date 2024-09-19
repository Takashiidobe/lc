# @leet start
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        This question asks us to find a subarray, where the length is at least 2,
        and the sum of the elements in the aubarray is a multiple of k.

        We can do this in $O(n^3)$ time by finding the sums of all the subarrays
        and checking them. This solution finds this in $O(n)$ time.

        We iterate once through the array, keeping track of the prefix modulus
        of the array. If we have seen the same prefix modulus before, we make
        sure we saw it at least an index of at least 1 away, so the length of
        the subarray is 2.
        """
        prefix_mod = 0
        mod_seen = {}

        for i, num in enumerate([0] + nums):
            prefix_mod = (prefix_mod + num) % k

            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i

        return False


# @leet end


def test():
    assert 2 + 2 == 4
