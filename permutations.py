# @leet start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        To calculate the permutations of an array, we first note what we want to do:
        if we're given just one item, the permutation is just that item.
        If we're given two items, we want to take the previous iteration
        and add the second item to the beginning and end, returning 2 items.
        For the third one, we take the previous 2 items (0, 1), (1, 0)
        and we want to add the third item in the beginning, middle, and end for
        both previous items.
        To do this, we first iterate through all the given numbers,
        and create an array that contains all the items for this iteration.
        Then, for each of the previous round's members, we want to iterate
        from beginning to one past the end and we add the current number to
        every index.
        Finally, in each iteration, we replace the previous round's result with
        our current round's result.
        """
        res = [[]]

        for num in nums:
            new_res = []
            for curr in res:
                for i in range(0, len(curr) + 1):
                    new_res.append(curr[:i] + [num] + curr[i:])
            res = new_res

        return res


# @leet end
q = Solution().permute


def test():
    assert q([1, 2, 3]) == [
        [3, 2, 1],
        [2, 3, 1],
        [2, 1, 3],
        [3, 1, 2],
        [1, 3, 2],
        [1, 2, 3],
    ]
