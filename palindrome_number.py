# @leet start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        This asks us to check if a number is a palindrome. We can do this
        by converting it into its digits and checking if the number is the
        same forwards and backwards
        """
        if x < 0:
            return False

        l = []
        while x:
            x, digit = divmod(x, 10)
            l.append(digit)
        rev_l = list(reversed(l))
        return l == rev_l


# @leet end


def test():
    assert 2 + 2 == 4
