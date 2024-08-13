from functools import cache


# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        To solve this question of the longest common subsequence, note that
        for both the strings, we have three choices.
        1. Either string is empty, in which case the LCS is 0.
        2. The first character of both strings is equal, in which case
        we return 1 + the LCS of the remaining strings incremented by 1.
        3. The characters do not match, in which case our LCS is the max of
        the LCS if we increment either side.

        We add some caching to this to reduce the time complexity from $O(2^m + n)$
        to $O(m * n)$, with $O(m * n)$ space complexity.
        """

        @cache
        def dfs(p1, p2):
            if not p1 or not p2:
                return 0
            if p1[0] == p2[0]:
                return 1 + dfs(p1[1:], p2[1:])
            else:
                return max(dfs(p1, p2[1:]), dfs(p1[1:], p2))

        return dfs(text1, text2)


# @leet end


def test():
    assert 2 + 2 == 4
