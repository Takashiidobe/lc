# @leet start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        To solve this question, we have to create a stack, finding
        out which items reach the same position before the target.

        We know that any cars that have a position after a given car but a higher
        speed could meet before the target, merging to create a group.
        Thus, we should figure out a way to distinguish which cars reach a target
        before a given time.

        To find out the number of car fleets, we need to sort the cars by
        position, and then speed in reverse order.
        We then iterate through the cars and figure out how many cars make a fleet.

        For every car, we check the current fleet. If there isn't one, the current
        car will become the fleet, and we move onto the next car.

        If there is a fleet, we check to see if our current car will intersect
        with the current fleet. If so, then we can add it to the current fleet,
        and thus disregard it.

        If the current car does not intersect with the current fleet, we start
        a new one.

        Finally, we return the number of fleets.
        """
        stack = []

        for pos, s in sorted(zip(position, speed), reverse=True):
            eta = (target - pos) / s
            if not stack or eta > stack[-1]:
                stack.append(eta)

        return len(stack)


# @leet end


def test():
    assert 2 + 2 == 4
