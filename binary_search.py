# @leet start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        A classic iterative binary search algorithm.
        This starts out by setting two pointers to the ends of the array
        and finding the midpoint between them.
        Since python has biginteger promotion, we calculate the mid with (l + r) // 2.
        In a language with fixed-width integers, this can overflow, so (r - l) // 2 + l
        also works.

        So in a loop:
        If the mid is equal to the target, return the midpoint.
        If the midpoint is less than the target, then set the left to mid + 1.
        Otherwise, the midpoint is greater than the target, set right to mid - 1.

        This finds the number in $O(log{}n)$ time or exits the loop, at which point
        the function returns -1.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# @leet end


def test():
    assert 2 + 2 == 4
