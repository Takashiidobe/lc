# @leet start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        This question asks us to move the zeroes to the end of the array while
        keeping the relative order of the items in an array while using no
        extra space, and doing the mutation in place.

        To do this, we can iterate through the array once, while keeping an index
        to the last non-zero element.

        If we find a non-zero element, we swap the current number with the number
        at the index with zeroes, and advance both pointers.

        If we find a zero, we just advance the current pointer.

        Take an example of [0, 1, 0, 3, 12].
        We initialize a slow pointer to 0, which holds the index of the last non-zero
        number, and iterate through numbers

        [0, 1, 0, 3, 12]
         ^ we start off here, and find a 0, so we continue on.
        slow = 0
        [0, 1, 0, 3, 12]
            ^ we find a 1, and so we swap it with our slow pointer and increment both.
        slow = 0
        [1, 0, 0, 3, 12]
               ^ we find another 0, so we continue on.
        slow = 1
        [1, 0, 0, 3, 12]
                  ^ we find a non-zero item, so we swap it with our slow pointer index.
        slow = 1
        [1, 3, 0, 0, 12]
                      ^ we find a non-zero item, so we swap it with our slow pointer index.
        slow = 2
        [1, 3, 12, 0, 0]
                      ^ we find a zero, so we do nothing.
        slow = 3
        """
        pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


# @leet end


def test():
    assert 2 + 2 == 4
