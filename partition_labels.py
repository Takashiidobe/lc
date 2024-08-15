# @leet start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        To partition a string into as many parts as possible such that each
        letter appears in at most one part, we want to keep track of the minimum
        and maximum index each character appears in.

        Next, we want to interpret this as merge intervals, and merge all the
        overlapping intervals. This works, because we want to take the first interval
        (say, 0, 8) and then keep adding in the characters until we hit the 8th
        index. If we encounter a character which has a character outside of our
        current range, since we must include it, we have to widen our range to include
        that character.

        If we properly exit our last interval, and there are no characters that
        have a last occurrence outside said interval, we have created a valid
        partition. Thus, we can start a new one by just adding our current
        interval as the new partition.

        We repeat this and then at the end return the distance + 1 for each
        interval that's left, which solves the problem.
        """
        indexes = {}

        for i, c in enumerate(s):
            if c in indexes:
                indexes[c] = [min(i, indexes[c][0]), max(i, indexes[c][1])]
            else:
                indexes[c] = [i, i]

        intervals = list(indexes.values())
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]
            if prev_end > start:
                res[-1] = [prev_start, max(prev_end, end)]
            else:
                res.append([start, end])

        return [end - start + 1 for start, end in res]


# @leet end


def test():
    assert 2 + 2 == 4
