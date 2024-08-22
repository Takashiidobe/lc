from functools import cache


# @leet start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        This question asks us to find the number of distinct subsequences
        where t fits into s.
        This can be done in $O(2^n)$ time, where at every letter, you have two
        choices depending on whether or not the characters match.

        If the characters do not match, we only increment the pointer to s,
        because we want to continue the search.

        If the characters do match, we can either increment both or just increment
        s, so we add up the number of both and return that.

        Finally, the terminating conditions: if we hit the end of t, return 1.
        Otherwise, if we hit the end of s and we haven't hit the end of t, we return 0.
        """

        @cache
        def dp(i, j):
            if i == len(s) and j != len(t):
                return 0
            if j == len(t):
                return 1
            if s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)

        return dp(0, 0)


# @leet end


def test():
    assert 2 + 2 == 4
