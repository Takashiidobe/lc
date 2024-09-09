from bisect import bisect_left
import random


# @leet start
class Solution:
    """
    This question asks us to define a class, where, given a number of weights,
    it randomly selects an index according to those weights.

    One way to do this is to actually fill the range, where say given [1, 3]
    you would create a weighted array of [0, 2, 2, 2] that corresponds to indexes
    and then you would generate a random number within the range and that
    would work. However, in the case that the numbers are very large, say
    [1000000, 10000101, ...] we would need a very large array, and this would
    become memory inefficient. A better way is to give up $O(1)$ random
    generation in order to decrease the size of the array.

    We calculate the prefix sum of all the weights and save that. Then,
    we pick a random number from [0, 1] and then bisect left using that number
    on the prefix sums. This allows us to find a random index in $O(log n)$ time,
    but with an array that is the size of the weights $O(n)$, which is much faster
    than the previous solution.
    """

    def __init__(self, w: list[int]):
        total = sum(w)
        weights = [w[0] / total]
        for weight in w[1:]:
            weights.append(weights[-1] + weight / total)
        self.weights = weights

    def pickIndex(self) -> int:
        random_num = random.random()
        return bisect_left(self.weights, random_num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @leet end


def test():
    assert 2 + 2 == 4
