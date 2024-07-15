from functools import reduce


# @leet start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        In an array where each number is present twice except for one number,
        this function finds that number.
        The way it does this is by using xor.
        If you xor a number by itself, you get 0.
        So all of the numbers that show up twice reduce to 0, and the only number
        that shows up once remains.
        """
        return reduce(lambda x, y: x ^ y, nums)


# @leet end


def test():
    assert 2 + 2 == 4
