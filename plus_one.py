# @leet start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Given a number of digits, this returns the number + 1.
        To do this, we turn the list of digits into a number, and then add 1 to it.
        This can be done with `num = num * 10 + digit`.

        Then we return this to the list by calling int on every string digit
        in the string version of the int.
        """
        num = 0
        for digit in digits:
            num = num * 10 + digit

        num += 1

        return [int(n) for n in str(num)]


# @leet end


def test():
    assert 2 + 2 == 4
