# @leet start
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        This problem involves backtracking, where we have a choice on every square
        to either place a queen or not on the current square.
        We need to verify if the move is legal, and then try to place the square
        if it is, we place the queen and recurse through the rest of the board.
        This has $O(n!)$ time complexity and $O(n^2)$ space complexity.
        """

        def create_board(state):
            return ["".join(row) for row in state]

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                invalid_col = col in cols
                invalid_diagonal = curr_diagonal in diagonals
                invalid_anti_diagonal = curr_anti_diagonal in anti_diagonals

                if invalid_col or invalid_diagonal or invalid_anti_diagonal:
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty)
        return ans


# @leet end


def test():
    assert 2 + 2 == 4
