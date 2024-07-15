# @leet start
class MinStack:
    """
    This problem implements a min stack.
    A min stack supports `push`, `pop`, `top`, and retrieving the minimum of a stack
    in constant time.
    To do so, for each item, the stack keeps the minimum value it has seen so far.
    So each item in the stack is a tuple of (int, int), where the first item
    is the minimum up to the current point, and the second item is the item itself.
    This means that when adding to the stack, we need to check the stack top's minimum
    and compare it with our current value. If the previous minimum is smaller, keep that.
    If not, set the current minimum to the current value for the current item.
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            prev_min = self.stack[-1][0]
            self.stack.append((min(prev_min, val), val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end


def test():
    assert 2 + 2 == 4
