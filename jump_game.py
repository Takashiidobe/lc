# @leet start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        To figure out if we can reach the end of the game, we can iterate
        backwards.
        We then check if our index + the number can reach any further than
        our current best. If so, we update our position to the current index.
        At the end we make sure we can reach the start of the array, which
        means we can make it from start to finish.
        """
        last_pos = len(nums) - 1

        for i, num in reversed(list(enumerate(nums))):
            if i + num >= last_pos:
                last_pos = i

        return last_pos == 0


# @leet end


def test():
    assert 2 + 2 == 4
