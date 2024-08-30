# @leet start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        This question asks us to remove items from the string that would
        lead to unbalanced parentheses, and to return a string that has balanced
        parentheses.

        We can do this by going through the string with the valid parentheses
        algorithm, but also keeping the indexes in the stack. If we see an '(',
        we add the index to the stack. If we see a ')', we pop from the stack if
        it's non-empty, closing a paren, or, we have an extra paren, so we have
        to skip it when we iterate through the string again, so we add it to a
        set of indexes to skip.

        At the end of the iteration, we have a set of indexes in the stack that
        are for superfluous open parens, so we add that to the indexes to remove
        as well.

        Finally, we iterate through the string, and if our current index is in
        the set to remove, we don't add it to the final string.
        """
        stack = []
        to_remove = set()

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    to_remove.add(i)
                else:
                    stack.pop()
        for i in stack:
            to_remove.add(i)
        res = ("" if i in to_remove else c for i, c in enumerate(s))
        return "".join(res)


# @leet end


def test():
    assert 2 + 2 == 4
