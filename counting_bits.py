# @leet start
class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        This question asks for the count of all bits in a range from 0 <= n.
        To count the bits using an intrinsic, we can use integer.bit_count
        but I manually wrote an implementation and used it.
        The `n &= n - 1` trick counts the bits by always removing the last
        set bit.
        """

        def bit_count(n: int) -> int:
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count

        return [bit_count(x) for x in range(n + 1)]


# @leet end
q = Solution().countBits


def test():
    assert q(2) == [0, 1, 1]
    assert q(5) == [0, 1, 1, 2, 1, 2]
