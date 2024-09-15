# @leet start
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        """
        This question asks us to find which buildings in a list have an ocean
        view, where the ocean lies to the right of the building array.
        To solve this problem, we want to use a monotonically decreasing stack.
        Take [4, 3, 2, 1]. All buildings have an ocean view, because they are
        in decreasing order. However, [1, 2, 3, 4] only has one building with
        an ocean view, since 4 is the tallest building and obstructs all the others.
        This question also notes that buildings of the same height do not obstruct
        each other.

        So, to do this, we iterate through the heights, and push to a stack.
        If the current building is taller than the previous item in the stack
        (i.e. it obstructs the previous building), we pop that previous building
        from the stack. We do this in a while loop, because every new building
        could obstruct many possible buildings that we've already seen.
        At the end, we're left with a monotonically decreasing stack, so we
        return the indexes of the buildings.
        """
        stack = []
        for i, height in enumerate(heights):
            while stack and height >= stack[-1][0]:
                stack.pop()
            stack.append((height, i))
        return [i for _, i in stack]


# @leet end


def test():
    assert 2 + 2 == 4
