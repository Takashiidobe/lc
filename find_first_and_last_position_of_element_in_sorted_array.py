# @leet start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        This question asks us to find the first and last position of an element
        in a sorted array.
        To do this, we can bisect left and bisect right using binary search, finding
        the lowest and highest values where the value is the target.

        On the bisect left side, if we find the current value is equal to target,
        we set r = mid - 1 and continue the iteration.

        On the bisect right side, if we find the current value is equal to target,
        we set l = mid + 1 and continue the iteration.

        One thing to note is that if the value isn't found, we have to return
        [-1, -1], so for both functions, we can have a sentinel value, found,
        which we can return, denoting if we've found the target.
        We can use this to find out if we found the value or not.
        """
        n = len(nums)

        def left_side(l, r):
            found = False
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    found = True
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return (found, l)

        def right_side(l, r):
            found = False
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    found = True
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return (found, r)

        ((found_left, l), (found_right, r)) = left_side(0, n - 1), right_side(0, n - 1)
        if not found_left or not found_right:
            return [-1, -1]
        return [l, r]


# @leet end


def test():
    assert 2 + 2 == 4
