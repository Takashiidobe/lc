# @leet start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        This question asks to return if `n` is a happy number, which either
        ends at 1 or loops through the process where it is replaced by the sum
        of the square of its digits.

        To find the square of the digits of a number, we can do the following:
        ```py
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        ```
        where `total` is the new number.
        We then set the conditions, where looping returns False and if n == 1
        then we return true.

        Finally we recurse through, since we know there's either a loop or
        the number ends at 1.
        """
        visited = set()

        def num_to_sum(n):
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit**2
            return num_to_sum(total)

        return num_to_sum(n)


# @leet end


def test():
    assert 2 + 2 == 4
