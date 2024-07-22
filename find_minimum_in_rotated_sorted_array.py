# @leet start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]


# @leet end
q = Solution().findMin


def test():
    assert q([3, 4, 5, 1, 2]) == 1
