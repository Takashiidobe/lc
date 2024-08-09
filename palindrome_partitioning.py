# @leet start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def dfs(s, path, result):
            if not s:
                result.append(path)
                return
            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]], result)

        result = []
        dfs(s, [], result)
        return result


# @leet end


def test():
    assert 2 + 2 == 4
