# @leet start
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        The count of one bits in a number can be done by bitwise ANDing the
        number `n` with itself minus 1 `n - 1`.
        The reason why this works is that if a bit is set in `n`, in `n - 1`,
        its least significant bit will become 0.
        Thus, if we AND the numbers together, the least significant bit is removed.
        We count how many times we do this until the number hits 0 to remove
        all of the one bits.
        """
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count


# @leet end
sol = Solution()


def test():
    assert sol.hammingWeight(11) == 3
    assert sol.hammingWeight(128) == 1
