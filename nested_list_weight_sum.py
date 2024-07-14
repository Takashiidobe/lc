from collections import defaultdict


class NestedInteger:
    """@private"""

    def __init__(self, value=None):
        self.value: list | int = []
        if value:
            self.value = value

    def isInteger(self) -> bool:
        return self.value is int

    def add(self, elem: int):
        self.value.append(elem)

    def setInteger(self, value):
        self.value = value

    def getInteger(self) -> int:
        if self.value is int:
            return self.value
        raise RuntimeError("Get List must be called on a NestedInteger that is an int")

    def getList(self) -> list:
        if self.value is list:
            return self.value
        raise RuntimeError("Get List must be called on a NestedInteger that is a list")


# @leet start
class Solution:
    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        """
        This problem asks to implement a function that implements the sum for a list of `NestedInteger`s.
        The NestedInteger class can either be an integer or a list.
        The total of a List of NestedInteger is each NestedInteger multiplied by its depth, summed up.
        For example, take this list: `[[1, 1], 2, [1, 1]]`. There are four integers with depth 2, which are 1
        and one 2, which has depth 1. So, the total is 10.

        To solve this, we can first iterate through the list to determine each item's depth, and assign it to a dict.
        The depth has to be found either iteratively or recursively. This solution does it recursively.
        For each item, the function calls a subroutine that checks if the current number is an integer.
        If it is, it adds it to the dictionary with its current depth.

        If it is not, then for each item in the sublist, it recurses, adding 1 to its depth.

        Finally, each key -> value pair of depth -> numbers is multiplied together, and summed up.
        """
        depths = defaultdict(list)

        def recurse(curr: NestedInteger, depth: int):
            if curr.isInteger():
                depths[depth].append(curr.getInteger())
            else:
                for item in curr.getList():
                    recurse(item, depth + 1)

        for item in nestedList:
            recurse(item, 1)

        return sum(k * sum(v) for k, v in depths.items())


# @leet end
def test():
    pass
