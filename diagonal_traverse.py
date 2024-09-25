from collections import defaultdict


# @leet start
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        """
        This question asks us to return the diagonal traverse of a matrix,
        where for [[1,2,3], [4,5,6], [7,8,9]], the traverse goes up, then down,
        and reverses.

        Thus, we want to return a flattened traversal.

        To do so, note that the rows for the correct traversal look like this:

        (0, 0)
        (1, 0), (0, 1)
        (2, 0), (1, 1), (0, 2)
        (2, 1), (1, 2)
        (2, 2)

        Thus, we want to group rows based on the sum of their y and x coordinates.
        Also, since the traversal reverses from up and down, we know that we can
        reverse each level based on its parity (if the level is even or odd).
        We can just reverse each even numbered row with this traversal to get
        the correct answer.
        """
        m, n = len(mat), len(mat[0])
        rows = defaultdict(list)

        for y in range(m):
            for x in range(n):
                rows[y + x].append(mat[y][x])

        res = []
        for k, v in rows.items():
            if k % 2 == 0:
                v.reverse()
            res.extend(v)

        return res


# @leet end


def test():
    assert 2 + 2 == 4
