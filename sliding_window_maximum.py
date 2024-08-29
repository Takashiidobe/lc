from collections import deque


# @leet start
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        This question asks us to find the sliding window maximum. We could
        do this by having a deque of length `k` and calculating the max of
        it as we pop and add to the queue. This, however, takes $O(n*k)$ time,
        and thus times out.

        We want to do this in $O(n)$ time, which is doable, as long as we use
        a monotonically decreasing deque. So, we first check the last item
        in the queue to make sure that it's smaller than the number we're
        currently looking at. If not, we pop it in a while loop.

        At the end, we append our right hand side to it.

        We then check the left hand side, if our current left pointer has
        a value greater than the first item in the queue, we pop it.

        Finally, if our queue length is the size of the window, we add the
        first item of the queue to the output array, since it is the largest
        item in the window, and increment our left pointer.

        At the end of the iteration, we increment our right pointer.
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


# @leet end


def test():
    assert 2 + 2 == 4
