# @leet start
from collections import OrderedDict


class LRUCache:
    """
    LRU Cache involves evicting the last item that was used (get/put) if
    the capacity of the dict becomes too big.
    We'll use an ordereddict, although a regular dict works as well.
    When we get from the dict, we'll move it to the end of the dictionary.
    When we put, we'll move our current key to the end and then if the capacity
    is greater, then we'll pop the item from the start.
    """

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)

        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(False)


def test():
    assert 2 + 2 == 4
