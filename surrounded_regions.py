# @leet start
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        This problem says to capture any O's that are surrounded by X's and
        turn them into X's. O's cannot be captured if they are
        To do so, we DFS from the edges (where y == 0 or x == 0 or y == m - 1 or
        n == n - 1).

        For all the O's we find, we turn them into some other character, like '1'
        in this case so we know that they're uncapturable.
        Then at the end, we traverse the board one more time, turning the remaining
        O's to X's (since they're capturable), and then turning the 1's to O's
        (since they're uncapturable).
        """
        m, n = len(board), len(board[0])
        visited = set()

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not inbounds(y, x) or (y, x) in visited or board[y][x] != "O":
                return
            visited.add((y, x))
            board[y][x] = "1"
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dy, dx in dirs:
                new_y, new_x = dy + y, dx + x
                dfs(new_y, new_x)

        for y in range(m):
            for x in range(n):
                if y == 0 or y == m - 1 or x == 0 or x == n - 1:
                    dfs(y, x)

        for y in range(m):
            for x in range(n):
                if board[y][x] == "1":
                    board[y][x] = "O"
                elif board[y][x] == "O":
                    board[y][x] = "X"


# @leet end


def test():
    assert 2 + 2 == 4
