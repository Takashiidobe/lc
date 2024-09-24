from collections import defaultdict


# @leet start
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        This question asks us to return true if the given matrix is toeplitz,
        where every diagonal from top-left to bottom-right has the same elements.

        We can do this by iterating through the matrix and grouping items that
        are in the same diagonal, and then we find out if the diagonal all have
        the same items.

        To do so, note that all items on the same diagonal have the same slope.

        Imagine a matrix like:
        [1, 2]
        [2, 2]

        In this case, we want three groups:
        [2], [1, 2], [2].

        They have the (y, x) coordinates of:
        [(0, 0)]
        [(0, 1), (1, 0)]
        [(1, 1)]

        We can see that the middle set has the same slant if we do (y - x) or
        (x - y). We can then group them by that.
        This takes $O(M * N)$ time, with $O(M + N)$ space.

        We can, however, get rid of the space requirement by simply checking
        each matrix with its top-left or bottom-right corresponding member.
        This would take the same amount of time, but $O(1)$ space.
        """
        m, n = len(matrix), len(matrix[0])

        slants = defaultdict(set)

        for y in range(m):
            for x in range(n):
                slants[y - x].add(matrix[y][x])

        return all([len(x) == 1 for x in slants.values()])


# @leet end


def test():
    assert 2 + 2 == 4
