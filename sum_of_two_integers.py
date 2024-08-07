# @leet start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        To add two numbers without using the plus operator, we can go back
        to computer architecture class.
        To add two bits together, we can use AND and XOR, and a 3rd bit, which
        is the carry bit, which denotes if we need to add an additional 1 to our
        result.
        If we add 0 and 0 and have a carry bit, we get 1 and dont set the carry.
        If we add 0 and 0 and no carry bit, we get 0 and dont set the carry.
        If we add 0 and 1 and have a carry bit, we get 0 and set the carry.
        If we add 0 and 1 and no carry bit, we get 1 and dont set the carry.
        If we add 1 and 1 and have a carry, we get 0 and set the carry.
        If we add 1 and 1 and no carry bit, we get 0 and set the carry.

        There are two duplicates (the flip of 1, 0 with and without the carry).
        But this table sets up our input, we just want to follow the output.
        To calculate the carry bit, we can AND the two numbers together.
        To calculate the result, we can XOR the two numbers.
        We then continue onto the next digit in the bitstring.
        """
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & mask if b else a


# @leet end


def test():
    assert 2 + 2 == 4
