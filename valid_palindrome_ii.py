# @leet start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        This question asks us to find if a string is a palindrome if you can delete
        up to one character.

        We can do this by checking if a palindrome is valid from the inside or
        outside, and then if there's a character that breaks the palindromic
        invariant, we can skip it, by skipping the current character.
        """

        def is_valid(l, r, skipped):
            while l < r:
                if s[l] != s[r]:
                    if skipped:
                        return False
                    return is_valid(l, r - 1, True) or is_valid(l + 1, r, True)
                l += 1
                r -= 1
            return True

        return is_valid(0, len(s) - 1, False)


# @leet end


def test():
    assert 2 + 2 == 4
