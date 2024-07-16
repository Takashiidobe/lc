from math import inf


# @leet start
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        curr_end = -inf
        for start, end in intervals:
            if start >= curr_end:
                curr_end = end
            else:
                res += 1
        return res


# @leet end
sol = Solution()


def test():
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
