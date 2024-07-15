from heapq import heapify, heappop, heappush


# @leet start
class KthLargest:
    """
    This class implements returning the kth largest item in a stream.
    To do so, it uses a heap, and only maintains the top k elements.
    The heap keeps the k largest elements.
    When the length of the heap is greater than k, it pops the minimum item.
    Since python's heap is a min-heap by default, the first item is always the kth
    item.
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapify(self.nums)
        self.heap = nums

        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @leet end


def test():
    assert 2 + 2 == 4
