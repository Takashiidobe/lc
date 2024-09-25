# @leet start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        This question asks us if `s` is a subsequence of `t`. To find that out,
        we can use two pointers. We start out at the beginning of `s` and `t`.
        If the current char of `s`, $s_i$ is equal to the current char of `t`,
        $t_j$, we increment both `i` and `j` since we've found a match. Otherwise,
        this is a miss, so we only increment `j`, since we want to continue on
        for `t`. Finally, we make sure we've reached the end of `s`, so we make
        sure that `i` is equal to the length of `s`.
        """
        i, j, m, n = 0, 0, len(s), len(t)

        while i < m and j < n:
            l, r = s[i], t[j]
            if l == r:
                i += 1
            j += 1
        return i == m


# @leet end


def test():
    assert 2 + 2 == 4
