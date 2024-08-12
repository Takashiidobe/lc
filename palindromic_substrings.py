# @leet start
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        This question asks us to count the number of palindromic substrings
        We can do this by counting the even and odd length palindromes starting
        from a given index, and repeat that for all the indexes in the string.
        If we can expand a palindrome and its left and right pointers are the
        same, we know we've found a new palindrome, and can increment the count.
        """
        n = len(s)
        count = 0

        def expand(l, r):
            nonlocal n, count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)

        return count


# @leet end


def test():
    assert 2 + 2 == 4
