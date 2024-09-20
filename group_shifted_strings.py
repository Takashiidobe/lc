from collections import defaultdict


# @leet start
class ShiftedString:
    def __init__(self, s) -> None:
        self.s = s

    def __hash__(self) -> int:
        key = []
        for l, r in zip(self.s, self.s[1:]):
            key.append((ord(r) - ord(l)) % 26 + ord("a"))
        return hash(tuple(key))


class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        """
        This question asks us to group all strings that can either be right or
        left shifted with each other. For example, 'az' can be shifted into 'ba'
        by doing one right shift, which wraps around.

        To do this, we encode the rules into a hashmap and then return all the
        strings that hash to the same value.

        The hash consists of the amount of shifts from the previous character it
        is. We can zip and iterate through the string to find this out.
        """
        groups = defaultdict(list)
        for string in strings:
            groups[hash(ShiftedString(string))].append(string)

        return list(groups.values())


# @leet end


def test():
    assert 2 + 2 == 4
