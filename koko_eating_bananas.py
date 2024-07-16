from math import ceil


# @leet start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        This problem asks to find the rate `k` it takes for Koko to eat
        all the piles of bananas in `h` hours, given once she finishes a pile
        she can't move onto another pile, and there's no travel time.

        The naive solution involves iterating from 1 to the largest pile and
        checking if koko can eat all the bananas.
        This solution is $O(mn)$ time, since for each pile $n$, you have to check
        $m$ rates, from 1 to m.

        We can optimize this: there's a way to answer this problem in $O(n * \log{}m)$ time.
        This can be done by using binary search.
        If our rate `k` can eat the bananas in time, then `k+1` can as well, but is worse.
        Likewise, there's not a guarantee that `k-1` can solve the problem.
        So if too many bananas are eaten too quickly, we can reduce `k`.
        If not enough bananas are eaten, we can increase `k`.

        The solution has a trick though, instead of normal binary search, if koko
        can eat all the bananas, we set right = mid and continue recursing.
        Otherwise, we set left = mid + 1.

        When left == right, we've found the minimum rate. We can either return
        left or right at that point.
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_spent = sum(ceil(pile / mid) for pile in piles)

            if hours_spent <= h:
                right = mid
            else:
                left = mid + 1

        return right


# @leet end


def test():
    assert 2 + 2 == 4
