# @leet start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        To calculate the clockwise spiral traversal of a matrix, we
        first note the directions we go in, which are right, down, left, up.
        Second, note that we start at the origin (0, 0).

        We want to start by moving right, and then when we hit the end or a cell
        we've already visited, we want to move down, then left, then up.

        Note that the directions look like this:
        right: (0, 1)
        down: (1, 0)
        left: (0, -1)
        up: (-1, 0)

        So when we want to transition from one direction to the other, we can
        either define an explicit transition array and do modulo arithmetic
        to keep going in a circle, or we can use the following formula:

        `dx, dy = -dy, dx`.

        So, (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) -> (0, 1).

        We then collect the results of our traversal into an array.
        """
        m, n = len(matrix), len(matrix[0])
        dy, dx, x, y = 0, 1, 0, 0

        res = []

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        for _ in range(m * n):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not inbounds(dy + y, dx + x) or matrix[dy + y][dx + x] == ".":
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res


# @leet end


def test():
    assert 2 + 2 == 4
