# @leet start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        This question can be solved with backtracking.
        We can DFS through the board, just remembering to backtrack from the visited
        set after we realize that this board can't contain the word.
        """
        m, n = len(board), len(board[0])

        def inbounds(y, x):
            return 0 <= y < m and 0 <= x < n

        def search(word, visited, y, x):
            if not word:
                return True

            if not inbounds(y, x) or (y, x) in visited or board[y][x] != word[0]:
                return False

            visited.add((y, x))
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dy, dx in dirs:
                if search(word[1:], visited, dy + y, dx + x):
                    return True

            visited.remove((y, x))

        for y in range(m):
            for x in range(n):
                if search(word, set(), y, x):
                    return True

        return False


# @leet end


def test():
    assert 2 + 2 == 4
