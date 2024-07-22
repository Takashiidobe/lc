# @leet start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        This function rotates a matrix 90 degrees.
        To do so, it grabs the four outermost cells and then rotates them like this:
        ![Rotate](https://assets.leetcode.com/static_assets/media/original_images/48/48_angles.png)
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n % 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - i - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


# @leet end


def test():
    assert 2 + 2 == 4
