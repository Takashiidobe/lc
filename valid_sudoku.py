# @leet start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        This function calculates if a sudoku is valid.
        To do so, only the digits 1-9 are allowed for all rows, cols, and 3x3 boxes.
        The 3x3 box location can be calculated by (r // 3) * 3 + c // 3.
        """
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


# @leet end
def test():
    assert 2 + 2 == 4
