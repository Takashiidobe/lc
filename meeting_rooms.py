from itertools import pairwise


# @leet start
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        """
        This problem shows a schedule of meetings, unsorted, and asks if it's possible
        to make it to every meeting, granted no travel time (assume they're virtual meetings).
        To do this, we sort all meetings and make sure that the start time of the next meeting
        is always after the end time of the previous meeting.
        """
        return all(
            prev_end <= curr_start
            for (_, prev_end), (curr_start, _) in pairwise(sorted(intervals))
        )


# @leet end
sol = Solution()


def test():
    assert not sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
    assert sol.canAttendMeetings([[7, 10], [2, 4]])
