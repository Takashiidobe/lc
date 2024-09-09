class Iterator:
    def __init__(self, nums):
        pass

    def hasNext(self):
        pass

    def next(self):
        pass


# @leet start
class PeekingIterator:
    """
    This question asks us to create a peekable iterator from an iterator that
    has next and hasNext methods.

    To do this most cleanly, we can keep a pointer to the next item in the iterator
    that we've created, and then query if the iterator still has items to go.

    When we peek or check for hasNext, we simply check the next value we've stored
    is not None. For the next function, we raise StopIteration if it's None,
    and otherwise, we try to poll the iterator for its next value if it has
    a next value. If it doesn't, we set the next value to None, signalling to
    peek and hasNext that we have no more items to go.
    """

    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        return self._next is not None


# @leet end


def test():
    assert 2 + 2 == 4
