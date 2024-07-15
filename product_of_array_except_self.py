# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] * num)

        suffix = [nums[-1]]
        for num in list(reversed(nums))[1:]:
            suffix.append(suffix[-1] * num)
        suffix.reverse()

        res = []
        for i, num in enumerate(nums):
            prefix_index = i - 1
            suffix_index = prefix_index + 2

            total = 1

            if 0 <= prefix_index < len(nums):
                total *= prefix[prefix_index]
            if 0 <= suffix_index < len(nums):
                total *= suffix[suffix_index]

            res.append(total)

        return res


# @leet end


def test():
    assert 2 + 2 == 4
