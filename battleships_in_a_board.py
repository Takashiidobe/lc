# @leet start
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        """
        This question asks us to count the number of battleships in a board
        where a battleship is horizontal or vertical (1 x k) or (k x 1).

        We can do this straightforwardly with just a dfs. Since battleships
        are guaranteed not to be next to each other, a dfs works for this Q.
        """
        visited = set()
        m, n = len(board), len(board[0])

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not inbounds(y, x) or (y, x) in visited or board[y][x] == ".":
                return
            visited.add((y, x))
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dy, dx in dirs:
                dfs(dy + y, dx + x)

        count = 0
        for y in range(m):
            for x in range(n):
                if board[y][x] == "X" and (y, x) not in visited:
                    count += 1
                    dfs(y, x)
        return count


# @leet end


def test():
    assert 2 + 2 == 4
