# @leet start

from math import trunc


class Solution:
    def calculate(self, s: str) -> int:
        """
        This question asks us to evaluate a string which can contain numbers,
        spaces, and the four arithmetic operators, '+', '-', '*', '/', where
        the expression is provided in infix notation.

        Let's take an example, of '3+ 5 / 2',

        We first handle parsing of the 3, and keep that.
        Then we parse the plus operator, and when we do that,
        we want to add 3 onto the stack, and save the operator for later.
        We then parse the next number, 5, and then parse the next operator, /.
        When we parse '/', we want to evaluate it immediately, so we set it
        as our previous op and then find 2, and evaluate it, to get 2.
        Then we add it to the stack, and get 5.

        Make sure to add any of the four operators at the end of our string
        so we can handle the last expr.
        """
        curr = 0
        op = "+"
        stack = []

        for c in s + "+":
            if c.isspace():
                continue
            elif c.isdigit():
                curr *= 10
                curr += int(c)
            else:
                if op == "+":
                    stack.append(curr)
                elif op == "-":
                    stack.append(-curr)
                elif op == "*":
                    top = stack.pop()
                    stack.append(top * curr)
                elif op == "/":
                    top = stack.pop()
                    stack.append(trunc(top / curr))
                curr = 0
                op = c

        return sum(stack)


# @leet end


def test():
    assert 2 + 2 == 4
