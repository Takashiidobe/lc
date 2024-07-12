# @leet start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        This function calculates the power of a number to another number in Log(n) time.

        To do this in linear time, we simply turn x ^ n into x * n (n times).

        Since we have to do this in linear time, we have to take a max of log(n) operations.

        We can do this by recursively taking the n multiplications and dividing them by two.

        This works because, imagine (2 ^ 4), which is 16. This can be reduced to 4 * 4.
        Or (2 * n / 2) * (2 * n / 2). To generalize this, x ^ n, where n is even becomes:

        $$
        (x * n / 2) * (x * n / 2).
        $$

        For an odd power, we can't evenly divide the powers. Imagine we have to calculate
        2 ^ 5. We can't divide this in half cleanly.

        However, this can be reduced to (2 * 2) * (2 * 2) * 2, since we know that x ^ n
        is equal to x ^ (n - 1) * x.
        So for the odd case, we floor divide the power by 2 and then multiply it by x as well.

        We do this recursively and define the two base cases, which are when n = 1 and n = 0.
        When n = 0, we always return 1.
        When n = 1, we return x.
        When n % 2 == 0, we return pow(x, n // 2) * pow(x, n // 2).
        When n % 2 == 1, we return pow(x, n // 2) * pow(x, n // 2) * x.
        If n is negative, simply return 1 / pow(x, -n) (the inverse).
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            halved = self.myPow(x, n // 2)
            return halved * halved
        if n % 2 != 0:
            halved = self.myPow(x, n // 2)
            return halved * halved * x
        return 0

# @leet end
sol = Solution()

def test_even_pow():
    """Test the path where the pow is positive and even."""
    assert(sol.myPow(2, 4) == 16)

def test_odd_pow():
    """Test the path where the pow is positive and odd."""
    assert(sol.myPow(2, 5) == 32)

def test_zero():
    """Test the path where the pow is 0."""
    assert(sol.myPow(2, 0) == 1)

def test_pow_one():
    """Test the path where the pow is 1."""
    assert(sol.myPow(2, 1) == 2)

def test_negative_even():
    """Test the path where the pow is negative and even."""
    assert(sol.myPow(2, -2) == 1 / 4)

def test_negative_odd():
    """Test the path where the pow is negative and odd."""
    assert(sol.myPow(2, -3) == 1 / 8)
