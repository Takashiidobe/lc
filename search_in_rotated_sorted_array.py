# @leet start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        To search in a rotated sorted array in $O(log n)$ time, we have to do
        a modified binary search.

        We have three points, the left, mid, and right.
        If the array is sorted from left to mid, we can treat it as a normal
        binary search. However, if it isn't we have to do the modified binary search,
        where we go in the opposite direction.
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


# @leet end


def test():
    assert 2 + 2 == 4
