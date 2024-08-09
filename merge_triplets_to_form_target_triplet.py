# @leet start
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        """
        To solve this problem, we can merge two triplets by only selecting the
        max of both items in each triplet.
        So, we need to meet two criteria:
        1. All the items in target have to be in the right positions.
        2. Any triplet that has an item that is larger than that target cannot
        be used for the target triplet.

        We know 1 must be true (otherwise the problem isn't solvable) and we also
        know 2 must be true because say we have a triplet where any one of the items
        is greater than its value in target:
        target = [2, 4, 6]
        curr = [2, 4, 8]
        other = [3, 4, 6]
        Even if we have a triplet, other, which has a 6 in the right position,
        the max of 6 and 8 is 8, thus it cannot be used to match the triplet.

        So, we iterate through the list of triplets, excluding all triplets that
        have any value greater than the target.
        For all other triplets, we check if any of their values match the target.
        If so, they can be used in the final triplet.
        Finally, we check to make sure we have at least one of each item in the right
        place for the triplet, and if so, the triplet is solvable.
        """
        good = set()
        tx, ty, tz = target

        for triplet in triplets:
            x, y, z = triplet
            if x > tx or y > ty or z > tz:
                continue
            for i, val in enumerate(triplet):
                if val == target[i]:
                    good.add(i)

        return len(good) == 3


# @leet end


def test():
    assert 2 + 2 == 4
