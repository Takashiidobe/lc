# @leet start
from sortedcontainers import SortedList


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        This question asks us to find if we can decompose a given set of cards
        into `groupSize` groups that are all straights (the cards are in order).

        To do this, we can greedily iterate through the hand in sorted order.
        We first put the hand into a sorted list, and we try to create each group.
        To do so, we pick the minimum available card, and then, for the next
        groupSize - 1 cards, we make sure we have the cards to make a straight.
        If we don't, we return false.

        If at the end we process all of the cards, we return true.

        We can do this in $O(n)$ time if we use a counter and count backwards.
        """
        n = len(hand)
        if n % groupSize != 0:
            return False

        sorted_hand = SortedList(hand)

        while sorted_hand:
            min_val = sorted_hand.pop(0)
            for i in range(1, groupSize):
                if min_val + i not in sorted_hand:
                    return False
                sorted_hand.remove(min_val + i)

        return True


# @leet end
q = Solution().isNStraightHand


def test():
    assert q([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert q([1, 2, 3, 4, 5], 4) is False
