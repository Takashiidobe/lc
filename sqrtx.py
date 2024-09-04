# @leet start
class Solution:
    def mySqrt(self, x: int) -> int:
        r"""
        To calculate the square root of a given number rounded down, we can
        use Newton's method.
        The algorithm starts with a guess of $x_1 \gt 0$ and iteratively guesses
        an improved square root.
        $$
        x_{n+1} = \frac{1}{2} \left( x_n + \frac{a}{x_n} \right)
        $$

        We start out by checking if x is 1 or 0, since that means its square root
        would be 1 or 0.

        Then, the algorithm figures out a current and next guess for the square
        root. The next guess is (curr + x / curr) / 2. If the next guess is
        sufficiently far away from the current number, we continue on the loop
        making curr into the next guess and calculating the next guess.
        If there's not enough progress made during the iteration, we return
        the next guess.
        """
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            print(x0, x1)
            x0 = x1
            x1 = (x0 + x / x0) / 2
        return int(x1)


# @leet end


def test():
    assert 2 + 2 == 4
