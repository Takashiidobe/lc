# @leet start
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        This question asks us to find an element that is strictly greater than
        its neighbors, so `nums[i - 1] < nums[i] > nums[i + 1]`.

        There are three possible cases, where nums is sorted in ascending order,
        descending order, or the peak is somewhere in the middle.

        In the ascending case, we want to return the last element.
        In the descending case, we want to return the first element.
        In the case where the peak is in the middle, we want to return the case
        where nums[i] > nums[i + 1], for all the items in the array. We know
        this works, because if the previous item fit this criteria, it would be
        greater than its previous number (through induction) and also greater
        than its next number, so it fits the criteria.

        We can do a linear scan where we zip through the numbers and do this.

        However, we can do this in $O(log\{n})$ time as well. We can apply the
        same rule to find the peak element. We do binary search as usual, but
        the criteria becomes checking if the current mid is greater than the
        next item. If this is the case, we set the right pointer to mid, since
        it is the last possible peak element, and we don't need to look at all
        items after mid.

        In the other case, we set l to mid + 1, because this item isn't a peak
        element, and all items to the left are discarded.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


# @leet end


def test():
    assert 2 + 2 == 4
