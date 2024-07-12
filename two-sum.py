# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexes = {}
        for i, num in enumerate(nums):
            if num in indexes:
                return [indexes[num], i]
            else:
                indexes[target - num] = i
        return [-1, -1]



# @leet end
sol = Solution()

def test():
    assert(sol.twoSum([2, 7, 11, 15], 9) == [0, 1])
    assert(sol.twoSum([3, 2, 4], 6) == [1, 2])
    assert(sol.twoSum([3, 3], 6) == [0, 1])
