# @leet start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        This function generates the powerset of a given set.
        This can be done by starting out with the empty set, and then
        For each item in the set, adding the current number to the end
        of each subset and then adding that copy to the end of the current list

        So, this looks like:

        1. [] (empty)
        2. [], [1] (1)
        3. [], [1], [2], [1, 2] (1, 2)
        4. [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3] (1, 2, 3)
        """
        res = [[]]

        for num in nums:
            res.extend([curr + [num] for curr in res])

        return res


# @leet end


def test():
    assert 2 + 2 == 4
