# @leet start
from sortedcontainers import SortedList


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        This question requires us to just backtrack and find all of the combination
        sums. To do so, we have a visited set (so we don't do any extra work), and
        a res set, which stores all of our results.

        We backtrack through, where for every round, we add a candidate to our
        current sum, and at the top, we check to make sure the sum is the right
        amount.

        We use a sorted list to make hashing a little easier (otherwise it requires
        sorting the list before putting it in the visited set), and return
        the result.
        """
        visited = set()
        res = set()

        def traverse(curr_sum, path):
            if tuple(path) in visited:
                return
            if curr_sum > target:
                return
            if curr_sum == target:
                res.add(list(path))
                return

            visited.add(tuple(path))

            for candidate in candidates:
                path.add(candidate)
                traverse(curr_sum + candidate, path)
                path.remove(candidate)

        traverse(0, SortedList())
        return list(list(res))


# @leet end


def test():
    assert 2 + 2 == 4
