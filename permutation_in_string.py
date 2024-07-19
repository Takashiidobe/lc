from collections import Counter


# @leet start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        This question asks to check if `s1` or a permutation of `s1` is contained
        in `s2`.

        Take the first example, `ab` and `eidbaooo`. `ba` is in `s2`, so this
        is true.

        Since we want any ordering of the letters from `s1` to be in a substring
        of `s2`, we can hold a counter of `s1` and check for equality as we
        iterate through `s2`.

        The solution detailed is terse but could be optimized, since it always
        recreates the counter.

        The optimized way would be to maintain a counter and then when moving
        to the left, remove the character that falls outside of the window and
        adding in the new character to the counter.
        """
        left = Counter(s1)

        width = len(s1)

        for i in range(len(s2) - width + 1):
            right = Counter(s2[i : i + width])
            if left == right:
                return True

        return False


# @leet end
q = Solution().checkInclusion


def test():
    assert q("ab", "eidbaooo")
    assert q("ab", "eidboaoo")
    assert q("adc", "dcda")
