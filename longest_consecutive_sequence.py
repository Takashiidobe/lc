# @leet start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            curr_len, curr_num = 1, num
            max_len = max(max_len, curr_len)  # to handle the case of 1 item
            if num - 1 in num_set:
                continue
            while curr_num + 1 in num_set:
                curr_len += 1
                max_len = max(max_len, curr_len)
                curr_num += 1
        return max_len


# @leet end
sol = Solution()


def test():
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([0, 0]) == 1
