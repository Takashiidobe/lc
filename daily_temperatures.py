# @leet start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        This problem asks to find the next greater item in the list and
        return said distance for every item.

        The naive way of doing it is in $O(n^2)$ time. For each temperature,
        we run a for loop until we find the next greater temperature, and set it
        in the current index.

        There's an $O(n)$ solution that involves using a stack.
        We start off with an empty stack.
        For every temperature we encounter, we check the stack in reverse.
        If the current temperature is greater than the previous temperature, we
        pop it and set its day's value to the distance between our element and
        the previous element.

        We do this in a while loop to make sure that all temperatures that haven't
        found a higher temperature yet are taken care of.
        When we encounter a temperature higher than our current temperature,
        we add our current temperature to the stack, and wait for the next iteration.

        All items left on the stack have their days set to 0, and the array is returned.
        """
        days = [0 for _ in range(len(temperatures))]

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_index = stack[-1][1]
                days[prev_index] = i - prev_index
                stack.pop()
            stack.append((temp, i))
        return days


# @leet end
sol = Solution()


def test():
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
