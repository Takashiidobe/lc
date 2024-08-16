from functools import cache


# @leet start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        This question asks us to create a regular expression matcher that
        supports '.' which matches any single character, and '*', which matches
        zero or more characters. As well, '.*' matches zero or more of every
        character.

        So, you have to handle the case of '.*' first, where you can match
        anything up until the end of the string, so we can dfs through any
        index until the end.

        If we have a '.', we match any single character and continue, returning
        false if s is empty.

        If there's '[a-z]*', we match that character as many times as we can
        and dfs through any of those.

        At the end, we just make sure to follow the rules for '.' again since
        it can appear as a single character.
        """

        @cache
        def dfs(s, p):
            if not s and not p:
                return True

            if len(p) > 1:
                curr, after = p[:2]
                if curr == ".":
                    if after == "*":
                        return any(dfs(s[i:], p[2:]) for i in range(len(s) + 1))
                    if not s:
                        return False
                    return dfs(s[1:], p[1:])
                if after == "*":
                    i = 0
                    while i < len(s) and s[i] == curr:
                        i += 1
                    return any(dfs(s[x:], p[2:]) for x in range(i + 1))

            if not p:
                return not s
            if not s:
                return not p

            if p[0] == "." or s[0] == p[0]:
                return dfs(s[1:], p[1:])

            return False

        return dfs(s, p)


# @leet end


def test():
    assert 2 + 2 == 4
