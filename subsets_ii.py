# @leet start
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        This question asks us to find the subsets if there are duplicates.
        To do this, I just found all the subsets, and then collected the
        non-duplicate results in a set and then returned that list.
        """
        res = [[]]

        for num in nums:
            res.extend([curr + [num] for curr in res])

        res = set(map(lambda x: tuple(sorted(x)), res))

        return list(res)


# @leet end


def test():
    assert 2 + 2 == 4
