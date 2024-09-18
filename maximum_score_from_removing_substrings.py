# @leet start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        This question gives us a string, `s`, and two numbers, `x` and `y`,
        which are the points gained from removing `ab` and `ba` from the string
        respectively.

        We want to maximize the score from removing all the substrings.

        We can test every removal by DFSing in $O(2^n)$ time.
        We can test every removal in $O(n^2)$ time with caching, as a DP problem.
        The optimal solution can be done in $O(n)$ time.

        We can do this by first checking which string, `ab` or `ba` is more
        valued. We always want to remove the more valued one first, because
        that maximizes our score.

        Imagine a string `baba`, where `ab` is worth 1 and `ba` is worth 2.
        If we take `ab` first, then `ba`, we get 3 points.
        However, if we take `ba` twice, we get 4 points.
        Thus, we want to take as many `ba`s first, then take any remaining
        `ab`s. In the case they're equally valued, it doesn't matter which one
        we take.
        """
        order = [("a", "b", x), ("b", "a", y)]
        if x < y:
            order.reverse()

        res = 0
        for l, r, points in order:
            stack = []
            for c in s:
                if stack and stack[-1] == l and c == r:
                    stack.pop()
                    res += points
                else:
                    stack.append(c)
            s = stack
        return res


# @leet end


def test():
    assert 2 + 2 == 4
