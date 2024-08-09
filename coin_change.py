# @leet start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        The coin change problem asks us to find the minimum number of coins
        required to make change for an amount.

        The intuition is that to make the amount of 0, we need 0 coins,
        and where each amount = coin, we need 1 coin.

        Next, we know that we can make any amount n where n - coin is already in
        our dp array.

        For example, with [2, 3]
        To make 5, we can first take either a 2 or 3 and then another 2 or 3.
        So, this should cost 2 coins.
        If we wanted to make 10, we require 2 5s, or 4 coins.
        Thus, to make progress, we can iterate through the coins and set our
        current cost to 1 + dp[n - coin], and do this until we reach our amount.

        We can then return dp[amount] to finish off the problem.
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if len(dp) > coin:
                dp[coin] = 1

        for n in range(amount + 1):
            for coin in coins:
                if n - coin > 0:
                    dp[n] = min(dp[n], 1 + dp[n - coin])

        return -1 if dp[amount] == float("inf") else dp[amount]


# @leet end


def test():
    assert 2 + 2 == 4
