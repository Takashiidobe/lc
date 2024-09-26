# @leet start
class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        """
        This question asks us to find the interval list intersections between two
        lists of intervals where both lists are sorted.

        We can do this by going through both lists and seeing if there's any overlap
        in between our left and right pointers. If there is an overlap, we add it
        to our result array. Calculating overlap is [max(l[0], r[0]), min(l[1], r[1])]
        However, note that we might have lists like:
        [5, 15]
        [5, 10], [10, 15]
        Where the overlap would be [5, 10], [10, 15].
        So, when we choose to increment a pointer, we always want to increment the
        pointer that ends sooner. This is because the other pointer that ends later
        may still have some matching intervals that come after the other pointer.
        So, we use the end of of both pointers to find out what to increment.
        """
        i, j, m, n = 0, 0, len(firstList), len(secondList)
        res = []

        while i < m and j < n:
            (l_start, l_end), (r_start, r_end) = firstList[i], secondList[j]
            if (l_start <= r_start and l_end >= r_start) or (
                r_start <= l_start and r_end >= l_start
            ):
                res.append([max(l_start, r_start), min(l_end, r_end)])
            if l_end < r_end:
                i += 1
            else:
                j += 1

        return res


# @leet end
def test():
    assert 2 + 2 == 4
