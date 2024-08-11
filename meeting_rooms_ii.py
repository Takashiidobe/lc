from heapq import heappush, heappop
# @leet start


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """
        See this code in action:
        <https://pythontutor.com/render.html#code=from%20heapq%20import%20heappush,%20heappop%0A%0Adef%20meeting_rooms%28intervals%3A%20list%5Blist%5Bint%5D%5D%29%20-%3E%20int%3A%0A%20%20%20%20if%20not%20intervals%3A%0A%20%20%20%20%20%20%20%20return%200%0A%0A%20%20%20%20intervals.sort%28%29%0A%0A%20%20%20%20free_rooms%20%3D%20%5B%5D%0A%0A%20%20%20%20heappush%28free_rooms,%20intervals%5B0%5D%5B1%5D%29%0A%0A%20%20%20%20for%20start,%20end%20in%20intervals%5B1%3A%5D%3A%0A%20%20%20%20%20%20%20%20if%20free_rooms%5B0%5D%20%3C%3D%20start%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20heappop%28free_rooms%29%0A%0A%20%20%20%20%20%20%20%20heappush%28free_rooms,%20end%29%0A%0A%20%20%20%20return%20len%28free_rooms%29%0A%0Ameeting_rooms%28%5B%5B0,30%5D,%5B5,10%5D,%5B15,20%5D%5D%29&cumulative=false&curInstr=17&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false>

        This problem asks how many meeting rooms are required to handle
        a set of meetings, where the meetings start and end times are given.

        To solve this problem, we first sort the intervals, and create a heap
        that only contains the end times of the meetings.

        We add the first interval to the heap, and then for all the other intervals

        We check the earliest end time in the heap, which is denoted by `free_rooms[0]`.
        If our time isn't later than that end time, there are no free meeting rooms.
        Thus, we need to allocate a new one.

        Then we add our current end time to the heap.

        Finally, the length of the heap is the amount of meeting rooms required.
        """
        if not intervals:
            return 0

        intervals.sort()

        free_rooms = []

        heappush(free_rooms, intervals[0][1])

        for start, end in intervals[1:]:
            if free_rooms[0] <= start:
                heappop(free_rooms)

            heappush(free_rooms, end)

        return len(free_rooms)


# @leet end
q = Solution().minMeetingRooms


def test():
    assert q([[0, 30], [5, 10], [15, 20]]) == 2
