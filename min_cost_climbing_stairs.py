from functools import cache


# @leet start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        This question asks us to find the minimum cost of climbing stairs,
        where we can climb 1 or 2 stairs at every step, and each step
        has an associated cost, and we can start from step 0 or 1.

        We can solve this via DP:
        Take the array of [10, 15, 20, 25, 30]
        To get to the first step, 10, we pay 0.
        To get to the second step, 15, we pay 0.
        For the third step, we can either get there from the first or second
        step, so we have to either pay the first or second steps' cost.

        For any step `n`, this is the case, you have to pay the minimum steps
        of all the steps either one before or two before it.
        So we can use this knowledge to build the DP array:

        With this array:
        [10, 15, 20, 25, 30]
        any `n`'s cost is `min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`.

        So 20's cost would be:
        20 = min(10 + 0, 15 + 0) = 10
        25 = min(15 + 0, 10 + 20) = 15
        30 = min(10 + 20, 15 + 25) = 30
        top = min(15 + 25, 30 + 30) = 40
        """

        @cache
        def min_cost(i):
            if i <= 1:
                return 0

            down_one = cost[i - 1] + min_cost(i - 1)
            down_two = cost[i - 2] + min_cost(i - 2)
            print(i, min(down_one, down_two))
            return min(down_one, down_two)

        return min_cost(len(cost))


# @leet end


def test():
    assert 2 + 2 == 4
