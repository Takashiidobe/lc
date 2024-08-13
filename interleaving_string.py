from functools import cache


# @leet start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        This question asks us if we can interleave `s1` and `s2` to make `s3`.
        We can interleave `s1` and `s2` by checking if the first character of
        either string is equal to `s3` and then incrementing the pointer to
        either string.

        We have to consider 6 situations:
        1. If all three of the strings are None, we know we've created the string.
        2. If `s1` or `s2` is None, we check if the other string equals `s3`.
        3. If the first character of `s1`, `s2`, and `s3` are the same,
        we can choose to increment the pointer to either string.
        4. If only `s1` == `s3`, we can increment the pointer in `s1`,
        5. If only `s2` == `s3`, we can increment the pointer in `s2`.
        6. In every other case, we cannot interleave the string, so return False.

        We add some caching to this in order to reduce the time complexity from
        $O(2^m + n)$ to $O(m * n)$, with $O(m * n)$ space complexity.
        """
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False

        @cache
        def interleave(s1, s2, s3):
            if not s1 and not s2 and not s3:
                return True
            if not s1:
                return s2 == s3
            if not s2:
                return s1 == s3
            if s1[0] == s2[0] == s3[0]:
                return interleave(s1[1:], s2, s3[1:]) or interleave(s1, s2[1:], s3[1:])
            if s1[0] == s3[0]:
                return interleave(s1[1:], s2, s3[1:])
            if s2[0] == s3[0]:
                return interleave(s1, s2[1:], s3[1:])
            return False

        return interleave(s1, s2, s3)


# @leet end


def test():
    assert 2 + 2 == 4
