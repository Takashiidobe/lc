from collections import defaultdict


# @leet start
from sortedcontainers import SortedList


class TimeMap:
    """
    This class defines a time-based key-value store that can store
    multiple values for the same key at different timestamps, and retrieve
    the key's value at a certain timestamp.

    So, set takes 3 params, key, value, timestamp and sets the key to value
    at the given timestamp.

    Get takes 2 params, key and timestamp, and returns a matching value
    where prev_timestamp <= timestamp.

    To implement this, we store the timestamps in a dict of key -> SortedList
    and the values in a dict of (timestamp, key) -> value.
    When we set, we set the key -> timestamp and the (timestamp, key) -> value.
    When getting, we check the index of the timestamp to get by bisecting right
    on the key with the given timestamp, and returning the previous index.

    Finally, if that index is inbounds, we use the (timestamp, key) pair to get the value
    If its not in bounds, we return "".
    """

    def __init__(self):
        self.timestamps = defaultdict(lambda: SortedList())
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].add(timestamp)
        self.values[(timestamp, key)] = value

    def get(self, key: str, timestamp: int) -> str:
        idx = self.timestamps[key].bisect_right(timestamp) - 1
        if 0 <= idx < len(self.timestamps[key]):
            timestamp = self.timestamps[key][idx]
            return self.values[(timestamp, key)]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end


def test():
    assert 2 + 2 == 4
