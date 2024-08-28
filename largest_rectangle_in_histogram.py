# @leet start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        This question asks us to find the largest rectangle in a set of
        heights.

        We can do this in $O(n)$ time with $O(n)$ space, using a monotonic
        stack.

        We only want to keep the largest item we've seen so far on the stack, so
        if we see an item that's larger than the top of the stack, we pop it
        and immediately process it to see if it would create a larger rectangle
        than currently exists.
        After we're done processing those items, we add the current height + index to
        the monotonic stack.

        We also want to handle the edge case where either the start or end of heights
        could contain the largest rectangle, so we add a [0] at both ends.
        """

        max_area = 0
        stack = []

        for i, height in enumerate([0] + heights + [0]):
            while stack and stack[-1][0] > height:
                rect_height = stack.pop()[0]
                left = stack[-1][1]
                area = (i - left - 1) * rect_height
                max_area = max(area, max_area)

            stack.append((height, i))

        return max_area


# @leet end


def test():
    assert 2 + 2 == 4
