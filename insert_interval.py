# @leet start
class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        """
        This question asks us to insert an interval that's unsorted into an array
        of intervals.
        We can do what the problem says and treat it as merge intervals.
        """
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if prev_end >= curr_start:
                res[-1] = [prev_start, max(prev_end, curr_end)]
            else:
                res.append([curr_start, curr_end])

        return res


# @leet end


def test():
    assert 2 + 2 == 4
