import heapq


# @leet start
class Solution:
    """
    This solution finds the kth largest element of an array by using a heap.
    This finds the element in $O(k log n)$ time, which is faster than sorting.

    First, we create a copy of the heap, where every item is multiplied by -1.
    This turns the heap from a min heap into a max heap.
    Then, for k - 1 times, we pop from the top of the heap, and then return the last popped value,
    negated.

    This finds the kth largest item.

    The fastest way to do this is in $O(n)$ time, which uses quickselect, along with a median of medians method.
    It's a little complicated to do, and can be $O(n^2)$ in the worst case without using Median of Medians.
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for _ in range(0, k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)


# @leet end
sol = Solution()


def test():
    assert sol.findKthLargest([1, 2, 3], 2) == 2
    assert sol.findKthLargest([3, 2, 1], 2) == 2
