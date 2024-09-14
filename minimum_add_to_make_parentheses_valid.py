# @leet start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        To find the minimum amount of operations to make a set of parens valid,
        we need to count the number of valid parens as we would normally, but
        also handle when there are unbalanced closing parens.
        We then add up the length of the stack (unbalanced opening parens) and
        the length of the unbalanced closing parens.
        """
        stack = []
        unbalanced = 0

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        return len(stack) + unbalanced


# @leet end


def test():
    assert 2 + 2 == 4
