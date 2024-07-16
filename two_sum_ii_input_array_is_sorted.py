from bisect import bisect_right


# @leet start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        This question asks to find the two numbers in an array which sum to target
        As well, there are two changes: the array is sorted, and you must do this with
        $O(1)$ extra space.

        To do so, we have to binary search in the array.
        We can do this with a bisect_left or bisect_right, but keeping in mind that
        bisect left and bisect right return the insertion point in the array.
        In bisect_left's case, its the point where insertion would be before any other
        duplicates, and for bisect_right, it's the pointer where insertion would be after
        any other duplicates, rather than the actual location in the array.

        So, using bisect_right and checking the position before is easier, since this always give us
        the last item in the array, so a duplicate like nums = [0, 0], target = 0
        returns the last item in the array.

        One optimization exists: since we've already passed all items before while
        iterating, we can check the bisection starting at the next index.
        This would speed up the algorithm a bit but makes calculating the index to return
        a bit more cumbersome.
        """
        for i, num in enumerate(numbers):
            res = bisect_right(numbers, target - num)
            if numbers[res - 1] == target - num:
                return [i + 1, res]
        return [-1, -1]


# @leet end


def test():
    assert 2 + 2 == 4
