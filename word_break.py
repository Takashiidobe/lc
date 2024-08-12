from functools import cache


# @leet start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        This question asks us to see if we can use the words in `wordDict` as
        many times as we want to reconstruct the string `s`.

        To do this, we can dfs through the given word choices and cache
        our decisions, so if we get to the same choice more than once we
        don't have to redo the same computation.
        """

        @cache
        def dfs(s):
            if not s:
                return True
            return any(
                dfs(s[len(word) :]) if s.startswith(word) else False
                for word in wordDict
            )

        return dfs(s)


# @leet end


def test():
    assert 2 + 2 == 4
