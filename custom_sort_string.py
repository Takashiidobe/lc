from functools import cmp_to_key


# @leet start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        This question asks us to sort a string given a particular sorted order,
        passed in the function as a parameter. If a char is not in the sorted
        order provided, it can be placed anywhere in the string.

        First we create a dictionary of char -> index to use later.
        Then we define a custom sorting function that returns -1, 0, or 1, and
        then use `cmp_to_key` from functools to turn that into a sorting function.

        We then sort the sortable characters and add the unsortable characters
        to the end of the string.
        """
        sort_order = {c: i for i, c in enumerate(order)}

        def sorter(a, b):
            if a == b:
                return 0
            if sort_order[a] > sort_order[b]:
                return 1
            return -1

        sortable = []
        unsortable = []
        for c in s:
            if c in sort_order:
                sortable.append(c)
            else:
                unsortable.append(c)

        sortable.sort(key=cmp_to_key(sorter))
        return "".join(sortable + unsortable)


# @leet end


def test():
    assert 2 + 2 == 4
