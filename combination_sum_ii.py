from collections import Counter
# @leet start


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        This question asks us to find the combination sum, but instead of allowing
        any number to be used infinitely, each number can only be used once.

        To solve this problem, we can use a counter, since that contains
        the numbers and counts of each number.

        We dfs as normal as we would in combination sum, but instead of iterating
        through all the candidates, we iterate through the counter and we check
        to make sure the counter's value is greater than 1 indicating the number
        still exists in the counter.

        We then add that number to our list and dfs through the list, and pop
        and readd the item to the counter to reverse the backtracking.
        """
        result = set()
        counter = Counter(candidates)

        def dfs(total, l):
            if total > target:
                return

            if total == target:
                l = sorted(l)
                result.add(tuple(l))
                return

            for val, freq in counter.items():
                if freq <= 0:
                    continue
                counter[val] -= 1
                l.append(val)
                dfs(total + val, l)
                l.pop()
                counter[val] += 1

        dfs(0, [])
        return list(result)


# @leet end


def test():
    assert 2 + 2 == 4
