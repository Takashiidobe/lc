# @leet start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        This problem asks to evaluate reverse polish notation.
        The way to do this is to use a stack and ops, as you would in a stack VM.
        If we encounter a number, we put it onto the top of the stack.
        If we encounter an operator, we pop the last two numbers from the stack,
        apply the operation, and then put it on top of the stack.
        At the end, we return the top of the stack.
        This works because the numbers are preceded by their operation, so
        they are evaluated just when needed, and never after.

        For infix notation, you'd have to use either recursive descent or pratt
        parsing to handle this problem, since once you see a `+` or `-` operator,
        you have to keep parsing until you hit another `+` or `-` operator before
        you can resolve the current operator.
        """
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token in ops:
                top = stack.pop()
                prev = stack.pop()
                op = ops[token]
                stack.append(op(prev, top))
            else:
                stack.append(int(token))
        return stack.pop()


# @leet end


def test():
    assert 2 + 2 == 4
