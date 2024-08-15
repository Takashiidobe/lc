from functools import cache


# @leet start
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        This question asks if a parentheses string that contains either
        '(', ')' or '*' is valid, where '*' can be an empty string or either open
        or closed paren.

        You can do this either with DP in $O(n^2)$ time and $O(n^2)$ space
        or you can do it greedily in $O(n)$ time and $O(1)$ space.

        The greedy approach looks like this, where you iterate forwards and
        backwards through the string, and increment the open paren count when
        you encounter a '(' or a '*' and increment the close paren count when
        you encounter a ')' or a '*', otherwise decrement both.

        If through the loop either open or close count are < 0, we return False.
        """
        open_count = 0
        close_count = 0
        n = len(s) - 1

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                open_count += 1
            else:
                open_count -= 1

            if s[n - i] == ")" or s[n - i] == "*":
                close_count += 1
            else:
                close_count -= 1

            if open_count < 0 or close_count < 0:
                return False
        return True

    def dp(self, s: str) -> bool:
        """
        To do this in the DP fashion, we can note that '(' should increase
        our paren count by 1, ')' should decrease it by 1, and '*' can either
        increase (if acts as '('), decrease (as ')') or do nothing (as '') to the count.

        '*' can act as all outcomes, so when we encounter that, we have to DFS
        through all possible outcomes.

        We can then dfs through in each case, making sure our paren_count never
        drops below 0 and return the result.
        """

        @cache
        def dfs(s, paren_count):
            if paren_count < 0:
                return False
            if not s:
                return paren_count == 0
            if s[0] == "(":
                return dfs(s[1:], paren_count + 1)
            if s[0] == ")":
                return dfs(s[1:], paren_count - 1)
            return (
                dfs(s[1:], paren_count + 1)
                or dfs(s[1:], paren_count - 1)
                or dfs(s[1:], paren_count)
            )

        return dfs(s, 0)


# @leet end


def test():
    assert 2 + 2 == 4
