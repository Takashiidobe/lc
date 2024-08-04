# @leet start
class Solution:
    def trap(self, height: list[int]) -> int:
        """
        This question asks us to see how much water can be trapped in between
        bars, given their heights.
        We can solve this using two pointers:
        We close the window, and calculate the trapped water based on the
        difference between the maximum height and the current height.
        We update the maximum height each iteration.
        If the right side is greater than the left side, we only look at the
        left side, or vice versa.
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0

        while left < right:
            left_height, right_height = height[left], height[right]
            if left_height < right_height:
                left_max = max(left_max, left_height)
                ans += left_max - left_height
                left += 1
            else:
                right_max = max(right_max, right_height)
                ans += right_max - right_height
                right -= 1
        return ans


# @leet end


def test():
    assert 2 + 2 == 4
