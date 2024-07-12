from math import isclose
from collections import deque

# @leet start
class MovingAverage:
    """
    This class exists to calculate the moving average of a data stream.
    The constructor receives the size of the window, and the next function
    is called with a new value to insert and returns the current average of the window.

    One naive approach is to keep an array, and consistently append to it.
    You can then calculate the average by taking the sum of arr[len - size..] / size.
    This works, but the amount of space required is $O(n)$ with regard to calls to next.
    As well, there's a lot of redundancy -- you recalculate the sum of items even though
    all but one of them has changed, making the average calculation slow for larger values of $size$.

    To deal with both of these, we want to use a data structure that allows us to keep
    $size$ items, and also allow for easy removal from the beginning and easy appends.
    This is a queue data structure.

    To make the average calculation easier, we keep the running total of the queue alongside it.
    So, if the queue has more space, we simply add $val$ to the queue and to our running total.
    If the queue has no more space, we remove a value from the beginning of the queue,
    subtract its value from the running total (since it has been removed) and then add our value
    to both the queue and the running total. We then divide the total by the len to get the average.

    This means that average calculation is now $O(1)$ time, the queue takes $O(size)$ memory, and
    adding/removing from the queue also takes $O(1)$ time, which is optimal.
    """
    def __init__(self, size: int):
        self.size = size
        self.items = deque()
        self.curr_total = 0
        self.len = 0

    def next(self, val: int) -> float:
        if self.len < self.size:
            self.curr_total += val
            self.len += 1
            self.items.append(val)
            return self.curr_total / self.len
        else:
            evicted = self.items.popleft()
            self.curr_total += (val - evicted)
            self.items.append(val)
            return self.curr_total / self.len
# @leet end
def test():
    sol = MovingAverage(3)
    assert(sol.next(1) == 1)
    assert(sol.next(10) == 5.5)
    assert(isclose(sol.next(3), 4.66667, rel_tol=1e-03))
    assert(sol.next(5) == 6.0)
