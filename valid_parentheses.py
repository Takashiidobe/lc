# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        This function returns either true or false given a string of parentheses,
        braces, and brackets.

        A string is considered balanced if each opening member is closed
        `[{}]` is considered balanced, because the two outermost brackets are lined up,
        and the two innermost braces also line up.
        `[[]` is not considered balanced, because the first bracket has no closing bracket,
        even though the second opening bracket does.

        Thus, we go through the string and do two different things.
        1. If the character is an opening char, add it to a stack.
        2. If the character is a closing char, check to make sure it complements the char
        on the top of the stack. If the stack is empty or the char does not match, return false.
        This corresponds to a case like '{]'.

        To make this easier, we can create a key -> val mapping of opening to closing chars
        and a reverse mapping, where closing chars are mapped to opening chars.

        We do this so we only have to write the pairs once, i.e. '{' -> '}'.
        If we did this in every if else case, if we have to add a new pair, it would become cumbersome quickly.
        """
        mapping = {'{': '}', '[': ']', '(': ')'}
        reverse_mapping = {v: k for k, v in mapping.items()}
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            if c in reverse_mapping:
                if not stack:
                    return False
                top = stack.pop()
                if top != reverse_mapping[c]:
                    return False

        return not stack



# @leet end
sol = Solution()

def test_braces():
	assert(sol.isValid("{}"))

def test_parens():
	assert(sol.isValid("()"))

def test_brackets():
	assert(sol.isValid("[]"))

def false_cases():
    assert(sol.isValid("{}["))
    assert(sol.isValid("())"))
    assert(sol.isValid("[]}"))
    assert(sol.isValid("[[]"))
