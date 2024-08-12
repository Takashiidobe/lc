# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        To find the longest palindromic substring, we want to take each
        character in the string and then expand it by one on each side.
        If both of the expanded characters are the same, we can continue
        expanding the palindrome indefinitely.

        To do this for odd sized palindromes, we set our left and right pointer
        to be equal, and for even length palindromes, we set them one apart from
        each other.
        """
        n = len(s)
        res = ""
        max_len = 0

        def expand(l, r):
            nonlocal n, res, max_len
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    res = s[l : r + 1]
                    max_len = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            # expand from the center
            l, r = i, i
            expand(l, r)
            l, r = i, i + 1
            expand(l, r)

        return res


# @leet end


def test():
    assert 2 + 2 == 4
