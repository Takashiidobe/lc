from collections import defaultdict
from itertools import chain


# @leet start
class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        """
        This question asks us to find the diagonal traverse of a list of lists,
        where the lists could be jagged (i.e. are not a matrix) and the traversal
        is just down to up.

        This is pretty similar to Diagonal Traverse I, where the rows are grouped by
        the sum of their y and x coordinates, and then reversed.
        We do that and flatten the end list to get the final answer.
        """

        m = len(nums)
        rows = defaultdict(list)

        for y in range(m):
            for x, num in enumerate(nums[y]):
                rows[y + x].append(num)

        for v in rows.values():
            v.reverse()

        return list(chain(*rows.values()))


# @leet end


def test():
    assert 2 + 2 == 4
