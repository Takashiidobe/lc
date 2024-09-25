class BinaryMatrix:
    def get(self, row, col):
        pass

    def dimensions(self):
        pass


# @leet start
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        """
        This question asks us to find the leftmost column that has at least
        a one, and each row of the matrix is sorted in non-decreasing order.
        For this, we can start out at the top right and then move to the bottom
        left.

        We know that if the curr_row, curr_col is a 1, we can always go left
        and if it's a 0, we go down.
        We then return the previous column that we saw.
        This runs in $O(M+N)$ time.
        """
        m, n = binaryMatrix.dimensions()
        curr_row, curr_col = 0, n - 1

        while curr_row < m and curr_col >= 0:
            if binaryMatrix.get(curr_row, curr_col) == 0:
                curr_row += 1
            else:
                curr_col -= 1
        return curr_col + 1 if curr_col != n - 1 else -1


# @leet end


def test():
    assert 2 + 2 == 4
