from collections import defaultdict
from random import choice


# @leet start
class Solution:
    """
    This question asks us to randomly output the index of a given target number,
    where the class has been initialized with an array that may have duplicates.

    To do this, we can iterate through the numbers and generate a mapping of
    number -> [indexes]. Once we do that, in the pick call, we fetch the indexes
    that match target and return one of those indexes (using random.choice).
    """

    def __init__(self, nums: list[int]):
        self.indexes = defaultdict(list)
        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target: int) -> int:
        indexes = self.indexes[target]
        return choice(indexes)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @leet end


def test():
    assert 2 + 2 == 4
