from functools import cache


# @leet start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        This question asks us to find the edit distance of two strings, or the amount
        of insert, update, and delete operations to transform word1 to word2.

        So, we have a few cases:

        1. if l == r, then we know their edit distance is 0.
        2. If l is empty, we know the edit distance is the length of r
        3. If r is empty, we know the edit distance is the length of l
        4. If l[0] == r[0], we can increment our pointer
        5. Insertion increments the right pointer
        6. Updating increments both pointers
        7. Deletion increments the left pointer

        If we do an operation, we have to return 1 + the operation, but we always
        want the minimum cost, so we return the cost of the operation that
        results in the fewest operations

        This runs in $O(m * n)$ time.
        """

        @cache
        def dp(l, r):
            if l == r:
                return 0
            if not l:
                return len(r)
            if not r:
                return len(l)
            if l[0] == r[0]:
                return dp(l[1:], r[1:])
            insert = dp(l, r[1:])
            update = dp(l[1:], r[1:])
            delete = dp(l[1:], r)
            return 1 + min(insert, update, delete)

        return dp(word1, word2)


# @leet end


def test():
    assert 2 + 2 == 4
