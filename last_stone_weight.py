from heapq import heapify, heappop, heappush


# @leet start
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        This problem describes a game with a list of stones.
        At every turn, we take the top 2 stones by weight and compare them.
        If they have the same weight, they are removed.
        Otherwise, the difference remains and is readded to the collection.
        At the end of the game, there's either 0 or 1 stone left.
        If there's no stones left, return 0. If there's 1, return its weight.

        We approach this with a heap. We first multiply each stone weight by -1
        to turn python's min-heap into a max heap.
        Then, while there are two stones, we follow the rules: If they are the same weight,
        remove them from the heap, otherwise, readd in the difference.
        At the end, reverse the sign again to recover the correct weights and either
        return 0 if the collection is empty or the last stone's weight.
        """
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        while len(stones) > 1:
            top = heappop(stones)
            next_top = heappop(stones)
            if top != next_top:
                diff = top - next_top
                heappush(stones, diff)

        if stones:
            return -stones[0]
        else:
            return 0


# @leet end
sol = Solution()


def test():
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1]) == 1
