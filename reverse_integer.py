# @leet start
class Solution:
    def reverse(self, x: int) -> int:
        """
        This function reverse an integer by using modulo on each digit in the
        and putting it in a variable called res.
        """
        sign = -1 if x < 0 else 1
        x *= sign

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= sign

        if res > 2**31 - 1 or res < -(2**31):
            return 0

        return res


# @leet end
q = Solution().reverse


def test():
    assert q(123) == 321
    assert q(-123) == -321
    assert q(120) == 21
