from collections import defaultdict


# @leet start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        This question asks us to find the longest substring where vowels have
        an even count. The brute force way is to iterate through all the substrings
        and maintain a vowel count while doing so, in $O(n^2)$ time. We can
        however, do better. Since we only care about the parity of the vowels
        we can use XOR to find this out in one pass, for $O(n)$ time.

        To do so, we create a bitmask which is XORed into to figure out when
        we've seen the same amount of even vowels again.

        Say we create a mapping of:
        a = 1
        e = 2
        i = 4
        o = 8
        u = 16

        If we create a bitmask of these, and xor each character, we can save the
        last time we've seen this particular bitmask. In that case, we know that
        our vowel counts are even, since XOR takes care of that (all even counts
        will XOR to 0).

        So we just keep track of the last time we saw a bitmask, and then if we see
        it again, we may have a longer substring, so we check that.
        """
        start = {0: -1}
        mask = 0
        chars = defaultdict(int) | {c: 1 << i for i, c in enumerate("aeiou")}
        res = 0

        for i, c in enumerate(s):
            mask ^= chars[c]
            if mask in start:
                res = max(res, i - start[mask])
            else:
                start[mask] = i
        return res


# @leet end


def test():
    assert 2 + 2 == 4
