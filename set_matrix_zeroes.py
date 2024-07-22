# @leet start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        This problem asks to set a row and col to zero if it contains
        an element that has a 0 in it.

        The way we do this is by keeping track of the rows and cols that have
        a 0, and then for each row and col that was zero,
        iterating through until we have set the entire row or col to 0.
        """
        rows = set()
        cols = set()

        m, n = len(matrix), len(matrix[0])

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    rows.add(y)
                    cols.add(x)

        for row in rows:
            for x in range(n):
                matrix[row][x] = 0

        for col in cols:
            for y in range(m):
                matrix[y][col] = 0


# @leet end


def test():
    assert 2 + 2 == 4
