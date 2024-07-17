# @leet start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        This problem asks to generate all balanced parentheses strings given
        a number `n`, the count of open and closed parens.

        Since we have two choices at every branch (either add an opening or closing paren)
        We know this is going to be $2^n$ time at least, so the input size cannot be big.

        So for every string, we can either add an opening or a closing paren.
        If the count of open parens == closed parens, then we can only add an open paren.
        If the count of open parens > closed parens, we can only add an open paren.

        We know this because if there's an empty string and a closed paren is added,
        the parens become unbalanced. Thus, any state which is equivalent to an empty string
        (when the count of open parens == closed parens), we can only add an open paren.
        """
        res = []

        def recurse(s):
            left = s.count("(")
            right = s.count(")")
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                recurse(s + "(")

            if right < n and right < left:
                recurse(s + ")")

        recurse("")

        return res


# @leet end
sol = Solution()


def test():
    assert sol.generateParenthesis(0) == [""]
    assert sol.generateParenthesis(1) == ["()"]
    assert sol.generateParenthesis(2) == ["()()", "(())"]
    assert sol.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
