# @leet start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Merge intervals takes any overlapping intervals and coalesces them into one interval.
        To do so, we first sort the intervals, and then compare the intervals pairwise.
        We want to look at the previous interval and the current interval.
        If the current interval's start is <= the previous end, then we know they are overlapping.
        In such a case, pick the minimum start and the maximum end to combine the two intervals.
        Set this as the previous interval.
        Otherwise, add the interval since they dont have any overlap.
        """
        intervals.sort()
        res = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if curr_start <= prev_end:
                res[-1][0] = min(prev_start, curr_start)
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append([curr_start, curr_end])

        return res


# @leet end
sol = Solution()


def test():
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
