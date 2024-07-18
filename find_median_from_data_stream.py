from heapq import heappush, heappop


# @leet start
class MedianFinder:
    """
    This class finds the median of a stream of integers.
    It does this by maintaining two heaps.
    The low heap is a max-heap, to store the smaller half of the numbers.
    The high heap is a min-heap, to store the higher half of the numbers.

    When adding an item from the stream, the number is first added in inverse
    to the max-heap.
    Then, the largest item from the max-heap is moved to the min-heap.
    Finally, if the min-heap is larger than the max-heap, the smallest number
    from the min-heap is added to the max-heap.

    When checking for the median, if the lengths of the two heaps are equal,
    we take the sum of the top of both of the heaps and divide by two.
    Otherwise, the max-heap is longer, and the top of the max-heap inverted
    is the median, since it has a length % 2 == 1.
    """

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @leet end


def test():
    assert 2 + 2 == 4
