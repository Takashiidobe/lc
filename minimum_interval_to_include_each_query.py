from heapq import heappush, heappop


# @leet start
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        This question asks us to find the smallest interval that contains a
        set of queries, passed in as an array.

        The brute force way of solving this problem involves an $O(n * q)$ solution,
        where for each query, you iterate through the intervals array and calculate
        the smallest interval that contains each query.

        We can do better by sorting both the intervals and queries, reducing
        runtime to $O(n log n + q log q)$, by using $O(n)$ space for a heap
        to contain intervals, and $O(q)$ space to cache all queries.

        We need the query cache because there can be duplicates as we iterate
        through the sorted queries.

        We iterate through the sorted queries and while we still have
        intervals left, and our current query fits inside the current interval,
        we add the interval to the heap. Next, while we've passed any intervals
        that can no longer contain our query, we pop those out of the heap.

        At the end, the top item of the heap contains the shortest interval.
        If there is none, we set our cache for q to -1.

        At the end, we return res[q] for each query.
        """
        intervals.sort()
        h, res, i = [], {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] < q:
                l, r = intervals[i]
                heappush(h, (r - l + 1, r))
                i += 1

            while h and h[0][1] < q:
                heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]


# @leet end


def test():
    assert 2 + 2 == 4
