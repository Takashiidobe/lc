# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        The best buy/sell pair is determined by the minimum price that comes before
        the largest price.
        We keep track of the minimum price we've seen so far, and the max profit,
        which is curr - min_so_far.
        Finally, we return the maximum profit after we've applied it to the entire array.
        """
        min_so_far = prices[0]
        max_profit_so_far = 0

        for price in prices[1:]:
            min_so_far = min(min_so_far, price)
            max_profit_so_far = max(max_profit_so_far, price - min_so_far)

        return max_profit_so_far


# @leet end
s = Solution()


def test():
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 5, 4, 3, 2, 1]) == 0
