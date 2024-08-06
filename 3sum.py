# @leet start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Three sum involves finding all triplets in a list that sum to 0.
        To do this, we can iterate through the array, fixing one number as our
        third number, and then solving 2 sum on the remaining items.

        To make this easy with two pointers, we first sort the nums, and then
        iterate through the numbers. Since our numbers are sorted, and we dont
        want to accept duplicates, we can skip duplicates with the condition
        i > 0 and a == nums[i - 1].
        We then check all the numbers to the right of the current number, and
        check if we have a matching triplet. If we do, we add it to the list.
        If our sum is too large, we decrement the right pointer to decrease the
        sum, and if the sum is too small, increment the left pointer to increase
        the sum.

        Finally, while we loop through the array, since duplicates can persist,
        we want to keep incrementing the left pointer as long as its the same number.
        """
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


# @leet end


def test():
    assert 2 + 2 == 4
