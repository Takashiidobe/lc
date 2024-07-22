# @leet start
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        We can find the bits of an integer by checking each bit and anding it with
        1 to see if it is set.
        Then for each bit in the output, we set it by bitwise ORing it in the location
        it needs to go.

        This solution goes bit by bit, but an optimized solution might go byte
        by byte and using shifting with a mask, but that's more complicated.
        """
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << 31 - i
        return res


# @leet end
q = Solution().reverseBits


def test():
    assert q(4294967293) == 3221225471
