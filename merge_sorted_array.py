# @leet start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        This question asks us to merge two sorted arrays, where one array has
        space for the other array.

        To do this optimally, we can do this in reverse, where we have 3 pointers:

        1. Pointer that starts at the end of the array
        2. One pointer at the end of nums1
        3. One pointer at the end of nums2

        We compare the two pointers at nums1 and nums2, and we put the larger
        one at the end of the array and decrement the pointer that had the larger
        number.

        We do this, while making sure to handle edge cases, like when we've exhausted
        the numbers in either array. If that's the case, we want to put the other
        number into the right place.
        """
        i = m - 1
        j = n - 1

        for k in range(m + n - 1, -1, -1):
            if i < 0 or (j >= 0 and nums1[i] < nums2[j]):
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1


# @leet end


def test():
    assert 2 + 2 == 4
