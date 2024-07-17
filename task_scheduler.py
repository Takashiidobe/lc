from collections import Counter


# @leet start
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        This question gives a list of CPU tasks, given the letters A - Z
        And a cooling time, `n`. Each cycle allows the completion of 1 task.
        However, you must wait `n` cycles before doing the same task again.

        To solve this problem, we can use a math formula.
        There are `max_count` - 1 occurrences, and `N + 1` refers to the
        cycles for cooldown + 1 for the actual instruction.

        So all we do is find the most frequent items, find how many of those
        there are, and then apply the formula, or the amount of tasks without cooldown.
        """
        freq = Counter(tasks)
        max_count = max(freq.values())

        time = (max_count - 1) * (n + 1)
        increment = sum([1 for val in freq.values() if val == max_count])

        return max(len(tasks), time + increment)


# @leet end


def test():
    assert 2 + 2 == 4
