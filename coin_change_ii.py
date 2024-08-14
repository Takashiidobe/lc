# @leet start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        """
        This question asks us to find the number of ways to make an amount
        given an array of coins.

        To do this, we want to create unique paths consisting of coins that
        sum up to the total amount. Since each coin can be taken infinitely
        many times, we want to dfs through the coins where we can either take
        our current coin or choose to skip it.

        So we can dfs where we always choose to take our current coin and
        the next coin in order to find the ways we can get the answer.

        At the end, there are three cases:
        1. Curr == amount. Return 1 for the amount of ways to get here.
        2. Curr > amount. Return 0, since this is invalid.
        3. i > len(coins). We've used up all the coins. Return 0.

        Finally, we need to build up our memoization table:
        We need to create a two dimensional array that contains all the valid ways
        we can reach our current location, and have a unique cache key, which
        can be the current coin we're on + the amount we've gotten.

        Finally, we set that value to either taking the current coin or skipping
        and then return that value, so we can continue the recursion for all other
        iterations.
        """
        cache = {}

        def dfs(i, curr):
            if curr == amount:
                return 1
            if curr > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, curr) in cache:
                return cache[(i, curr)]

            cache[(i, curr)] = dfs(i, curr + coins[i]) + dfs(i + 1, curr)
            return cache[(i, curr)]

        return dfs(0, 0)


# @leet end


def test():
    assert 2 + 2 == 4
