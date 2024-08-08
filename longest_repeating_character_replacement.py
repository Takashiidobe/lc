from collections import Counter


# @leet start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string s, and an integer k, the amount of replacements
        allowed, we want to return the length of the longest string.
        If we iterate through, we can add every char c one by one into our counter.
        when len(counter) - max(counter) <= k, we have a valid max len
        if we get to a state where that is not the case, we continue removing
        characters from the beginning of our sliding window until we hit
        the case where it is true again and increment our right pointer.
        """
        l = 0
        c = Counter()
        max_len = 0
        for curr in s:
            c[curr] += 1
            while sum(c.values()) - max(c.values()) > k:
                c[s[l]] -= 1
                l += 1
            max_len = max(max_len, sum(c.values()))

        return max_len


# @leet end


def test():
    assert 2 + 2 == 4
