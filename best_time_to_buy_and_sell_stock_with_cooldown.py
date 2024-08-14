from functools import cache


# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        This question asks us to calculate the max profit for buying + selling
        as many stocks as we want, given a 1 day cooldown after selling a stock.

        Therefore, on any given day, there are 3 choices you have:
        1. Do nothing (pass)
        2. Buy (where you want to minimize the current minimum price seen)
        3. Sell (where you want to maximize the profit by buying the stock at
        the minimum you've seen so far, and selling it at the current price,
        and applying the cooldown rule)

        We can translate those rules into a function and then cache its results.
        """

        @cache
        def traverse(i, curr_min, curr_max):
            if i >= len(prices):
                return 0
            curr_min = min(curr_min, prices[i])
            curr_max = max(curr_max, prices[i])
            buy = traverse(i + 1, curr_min, curr_max)
            sell = prices[i] - curr_min + traverse(i + 2, float("inf"), float("-inf"))
            return max(buy, sell)

        return traverse(0, float("inf"), float("-inf"))


# @leet end


def test():
    assert 2 + 2 == 4
