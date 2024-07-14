# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        This problem involves calculating the max area of a set of bars.
        The distance betwee each bar is 1, and the height of each bar is given.
        The naive solution involves testing each $n * (n - 1)$ combination of bars
        to find the highest area. This predictably takes $O(n^2)$ time, and takes
        the most amount of time possible (there are $n^2$ pairs, so testing all of them
        is the brute force approach.

        There's an $O(n)$ solution by removing checking $n - 1$ positions for each pair.
        The way to do that is by knowing that it's only possible to increase the area
        by either starting at the center or the ends.

        If we start at the center, every pair is possibly bigger, on both the left
        and right hand side. We'd still end up with an $O(n^2)$ solution, because
        we have to check both sides and we want to avoid that.

        If we start at the ends, however, we know that there's no possible way to increase
        the area unless we move the smaller bar in. If we move the larger bar in,
        then we always decrease the total area. However, if we move the smaller bar in,
        there is a chance there is a larger bar in between that can produce a larger area.

        We do this up to $O(n)$ times, and calculate the largest area in the array.
        """
        i, j = 0, len(height) - 1
        max_area_so_far = 0

        while i < j:
            left_height, right_height = height[i], height[j]
            area = (j - i) * min(left_height, right_height)
            max_area_so_far = max(area, max_area_so_far)
            if left_height < right_height:
                i += 1
            else:
                j -= 1

        return max_area_so_far


# @leet end
sol = Solution()


def test():
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
